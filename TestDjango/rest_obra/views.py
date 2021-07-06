from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from core.models import Obra
from .serializers import ObraSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))

def listado_obra(request):
    """
    Lista todos las obras
    """
    if(request.method=='GET'):
        ob=Obra.objects.all()
        serializer=ObraSerializer(ob, many=True)
        return Response(serializer.data)
    elif (request.method=='POST'):
        data=JSONParser().parse(request)
        serializer=ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_obra(request, id):
    """
    GET, UPDATE AND DELETE
    """

    try:
        ob = Obra.objects.get(nombreOb=id)
    except Obra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ObraSerializer(ob)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(ob, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
