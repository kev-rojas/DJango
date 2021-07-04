from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from core.models import Usuario
from .serializers import UsuarioSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))

def lista_usua(request):
    """
    Lista todos los usuarios
    """
    if(request.method=='GET'):
        usu=Usuario.objects.all()
        serializer=UsuarioSerializers(usu, many=True)
        return Response(serializer.data)
    elif (request.method=='POST'):
        data=JSONParser().parse(request)
        serializer=UsuarioSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def detalle_usuario(request, id):
    """
    GET, UPDATE AND DELETE
    """

    try:
        usu = Usuario.objects.get(email=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuarioSerializers(usu)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(usu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)