from django.shortcuts import render, redirect
from .models import vehiculo
from .forms import vehiculoForm
from .models import Usuario
from .forms import UsuarioForm
#-------------------------------------------------------------------

#def de ejemplos

def home(request):
    #return render(request,'core/home.html')
    #traer todos los vehiculos en la tabla
    vehiculos=vehiculo.objects.all
    #variable que pasa los datos del vehiculo al template
    datos={
        'vehiculos': vehiculos
    }
    return render(request, 'core/home.html', datos)

def form_vehiculo(request):
    dato={'form' : vehiculoForm}
    if request.method=='POST':
        formulario=vehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            dato['mensaje']="Guardado correctamente"
    return render(request, 'core/form_vehiculo.html',dato)

def form_modvehiculo(request,id):
    vehiculos=vehiculo.objects.get(patente='AABB11')
    datos={'form':vehiculoForm(instance=vehiculos)}
    if request.method=='POST':
        formulario=vehiculoForm(data=request.POST, instance=vehiculos)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request, 'core/form_modvehiculo.html',datos)

def form_delvehiculo(request,id):
    vehiculos=vehiculo.objects.get(patente=id)
    vehiculos.delete()
    return redirect(to="home")

#--------------------------------------------------------------------------------------------------


#def iniciales del proyecto

def inicio(request):
    return render(request,'core/inicio.html')

def artistas(request):
    return render(request,'core/artistas.html')

def inicarSesion(request):
    return render(request,'core/inicarSesion.html')

def almuerzo(request):
    return render(request,'core/almuerzo.html')

def balloon(request):
    return render(request,'core/balloon.html')

def cap(request):
    return render(request,'core/cap.html')

def capital(request):
    return render(request,'core/capital.html')

def cases(request):
    return render(request,'core/cases.html')

def chaosn2(request):
    return render(request,'core/chaosn2.html')

def cisnes(request):
    return render(request,'core/cisnes.html')

def comedores(request):
    return render(request,'core/comedores.html')

def conceptos(request):
    return render(request,'core/conceptos.html')

def coquelicots(request):
    return render(request,'core/coquelicots.html')

def corona(request):
    return render(request,'core/corona.html')

def crepusculo(request):
    return render(request,'core/crepusculo.html')

def cristo(request):
    return render(request,'core/cristo.html')

def cuadron19(request):
    return render(request,'core/cuadron19.html')

def damaarmiño(request):
    return render(request,'core/damaarmiño.html')

def discobolo(request):
    return render(request,'core/discobolo.html')

def elefantes(request):
    return render(request,'core/elefantes.html')

def elvacio(request):
    return render(request,'core/elvacio.html')

def frescos(request):
    return render(request,'core/frescos.html')

def ginebra(request):
    return render(request,'core/ginebra.html')

def guernica(request):
    return render(request,'core/guernica.html')

def guitarrista(request):
    return render(request,'core/guitarrista.html')

def habitacion(request):
    return render(request,'core/habitacion.html')

def hissam(request):
    return render(request,'core/hissam.html')

def hombrevitruvio(request):
    return render(request,'core/hombrevitruvio.html')

def impresion(request):
    return render(request,'core/impresion.html')

def interchange(request):
    return render(request,'core/interchange.html')

def jardin(request):
    return render(request,'core/jardin.html')

def judia(request):
    return render(request,'core/judia.html')

def lafuente(request):
    return render(request,'core/lafuente.html')

def leccion(request):
    return render(request,'core/leccion.html')

def lirios(request):
    return render(request,'core/lirios.html')

def mascara(request):
    return render(request,'core/mascara.html')

def memoria(request):
    return render(request,'core/memoria.html')

def metamorfosis(request):
    return render(request,'core/metamorfosis.html')

def moises(request):
    return render(request,'core/moises.html')

def monalisa(request):
    return render(request,'core/monalisa.html')

def mujerespejo(request):
    return render(request,'core/mujerespejo.html')

def mujerllorando(request):
    return render(request,'core/mujerllorando.html')

def nocheestrellada(request):
    return render(request,'core/nocheestrellada.html')

def nude(request):
    return render(request,'core/nude.html')

def obrasclaude(request):
    return render(request,'core/obrasclaude.html')

def obrasdali(request):
    return render(request,'core/obrasdali.html')

def obrasleonardo(request):
    return render(request,'core/obrasleonardo.html')

def obraspablo(request):
    return render(request,'core/obraspablo.html')

def obrasrembrant(request):
    return render(request,'core/obrasrembrant.html')

def obrasvincent(request):
    return render(request,'core/obrasvincent.html')

def pagartabs(request):
    return render(request,'core/pagartabs.html')

def pagartconc(request):
    return render(request,'core/pagartconc.html')

def pagartcont(request):
    return render(request,'core/pagartcont.html')

def pagartcub(request):
    return render(request,'core/pagartcub.html')

def pagesculturas(request):
    return render(request,'core/pagesculturas.html')

def pagorfebreria(request):
    return render(request,'core/pagorfebreria.html')

def pagpinturas(request):
    return render(request,'core/pagpinturas.html')

def pagtejidos(request):
    return render(request,'core/pagtejidos.html')

def paisaje(request):
    return render(request,'core/paisaje.html')

def pensador(request):
    return render(request,'core/pensador.html')

def rabbit(request):
    return render(request,'core/rabbit.html')

def registrarse(request):
    datos={'form' : UsuarioForm}
    if request.method=='POST':
        formulario=UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Registrado Correctamente"
    return render(request,'core/registrarse.html',datos)

def retorno(request):
    return render(request,'core/retorno.html')

def retrato(request):
    return render(request,'core/retrato.html')

def ronda(request):
    return render(request,'core/ronda.html')

def ruedadebicicleta(request):
    return render(request,'core/ruedadebicicleta.html')

def salvatormundi(request):
    return render(request,'core/salvatormundi.html')

def señoras(request):
    return render(request,'core/señoras.html')

def silla(request):
    return render(request,'core/silla.html')

def sindicato(request):
    return render(request,'core/sindicato.html')

def sombrilla(request):
    return render(request,'core/sombrilla.html')

def soporte(request):
    return render(request,'core/soporte.html')

def sueño(request):
    return render(request,'core/sueño.html')

def telefono(request):
    return render(request,'core/telefono.html')

def tentacion(request):
    return render(request,'core/tentacion.html')

def terraza(request):
    return render(request,'core/terraza.html')

def tesoro(request):
    return render(request,'core/tesoro.html')

def tipoobras(request):
    return render(request,'core/tipoobras.html')

def tormenta(request):
    return render(request,'core/tormenta.html')

def trigal(request):
    return render(request,'core/trigal.html')

def ultimacena(request):
    return render(request,'core/ultimacena.html')

def unaytressillas(request):
    return render(request,'core/unaytressillas.html')

def unroble(request):
    return render(request,'core/unroble.html')

def ventana(request):
    return render(request,'core/ventana.html')

def ventanas(request):
    return render(request,'core/ventanas.html')

def venus(request):
    return render(request,'core/venus.html')

def visigodo(request):
    return render(request,'core/visigodo.html')

def vives(request):
    return render(request,'core/vives.html')