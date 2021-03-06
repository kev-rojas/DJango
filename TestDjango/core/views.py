from django.shortcuts import render, redirect
from .models import Usuario, Obra, Contacto
from .forms import UsuarioForm, ContactoFrom, ObraForm
from django.contrib import messages
#-------------------------------------------------------------------

def consumeapi(request):
    mona=Obra.objects.get(nombreOb='La Mona Lisa')
    datos={
        'mona': mona
    }
    return render(request, 'core/consumeapi.html',datos)  

#------------------------------------------------------------------
def mod_obra(request,id):
    ob=Obra.objects.get(nombreOb=id)
    datos={'form':ObraForm(instance=ob)}
    if request.method=='POST':
        formulario=ObraForm(data=request.POST, instance=ob)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Modificado Correctamente")
    return render(request, 'core/mod_obra.html',datos)


def lista_usuarios(request):
    usua=Usuario.objects.all
    datos={
        'usua': usua
    }
    return render(request, 'core/lista_usuarios.html', datos)

def mod_usuario(request,id):
    usua=Usuario.objects.get(email=id)
    datos={'form':UsuarioForm(instance=usua)}
    if request.method=='POST':
        formulario=UsuarioForm(data=request.POST, instance=usua)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="lista_usuarios")
    return render(request, 'core/mod_usuario.html',datos)

def del_usuario(request,id):
    usua=Usuario.objects.get(email=id)
    usua.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="lista_usuarios")




def inicio(request):
    datos={'form' : ContactoFrom}
    if request.method=='POST':
        formulario=ContactoFrom(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Enviado Correctamente"
    return render(request,'core/inicio.html',datos)

def artistas(request):
    return render(request,'core/artistas.html')

def inicarSesion(request):
    usua=Usuario.objects.all
    datos={
        'usua': usua
    }
    return render(request,'core/inicarSesion.html', datos)

def almuerzo(request):
    almuerzo=Obra.objects.get(nombreOb='Almuerzo sobre la hierba')
    datos={
        'almuerzo': almuerzo
    }
    return render(request,'core/almuerzo.html',datos)

def balloon(request):
    ball=Obra.objects.get(nombreOb='Ballon Dog (Orange)')
    datos={
        'ball': ball
    }
    return render(request,'core/balloon.html',datos)

def cap(request):
    cap=Obra.objects.get(nombreOb='Cap de Fernande')
    datos={
        'cap': cap
    }
    return render(request,'core/cap.html',datos)

def capital(request):
    capi=Obra.objects.get(nombreOb='Letra Capital')
    datos={
        'capi': capi
    }
    return render(request,'core/capital.html',datos)

def cases(request):
    cas=Obra.objects.get(nombreOb='Cases d.Horta')
    datos={
        'cas': cas
    }
    return render(request,'core/cases.html',datos)

def chaosn2(request):
    cha=Obra.objects.get(nombreOb='Chaos N2')
    datos={
        'cha': cha
    }
    return render(request,'core/chaosn2.html',datos)

def cisnes(request):
    cis=Obra.objects.get(nombreOb='Cisnes que se reflejan como elefantes')
    datos={
        'cis': cis
    }
    return render(request,'core/cisnes.html',datos)

def comedores(request):
    com=Obra.objects.get(nombreOb='Los Comedores de Patatas')
    datos={
        'com': com
    }
    return render(request,'core/comedores.html',datos)

def conceptos(request):
    return render(request,'core/conceptos.html')

def coquelicots(request):
    coq=Obra.objects.get(nombreOb='Coquelicots')
    datos={
        'coq': coq
    }
    return render(request,'core/coquelicots.html',datos)

def corona(request):
    cor=Obra.objects.get(nombreOb='Corona de Recesvinto')
    datos={
        'cor': cor
    }
    return render(request,'core/corona.html',datos)

def crepusculo(request):
    cre=Obra.objects.get(nombreOb='Crepusculo en Venecia')
    datos={
        'cre': cre
    }
    return render(request,'core/crepusculo.html',datos)

def cristo(request):
    cri=Obra.objects.get(nombreOb='Cristo Redentor')
    datos={
        'cri': cri
    }
    return render(request,'core/cristo.html',datos)

def cuadron19(request):
    cua=Obra.objects.get(nombreOb='The Moon Woman Cuts the Circle')
    datos={
        'cua': cua
    }
    return render(request,'core/cuadron19.html',datos)

def damaarmi??o(request):
    mi??o=Obra.objects.get(nombreOb='Dama de Armi??o')
    datos={
        'mi??o': mi??o
    }
    return render(request,'core/damaarmi??o.html',datos)

def discobolo(request):
    dis=Obra.objects.get(nombreOb='El Disc??bolo')
    datos={
        'dis': dis
    }
    return render(request,'core/discobolo.html',datos)

def elfantes(request):
    ele=Obra.objects.get(nombreOb='Los Elefantes')
    datos={
        'ele': ele
    }
    return render(request,'core/elfantes.html',datos)

def elvacio(request):
    vac=Obra.objects.get(nombreOb='El Vac??o')
    datos={
        'vac': vac
    }
    return render(request,'core/elvacio.html',datos)

def frescos(request):
    fres=Obra.objects.get(nombreOb='Frescos Har??n Real')
    datos={
        'fres': fres
    }
    return render(request,'core/frescos.html',datos)

def ginebra(request):
    gine=Obra.objects.get(nombreOb='Ginebra de Vinci')
    datos={
        'gine': gine
    }
    return render(request,'core/ginebra.html',datos)

def guernica(request):
    guer=Obra.objects.get(nombreOb='Guernica')
    datos={
        'guer': guer
    }
    return render(request,'core/guernica.html',datos)

def guitarrista(request):
    guit=Obra.objects.get(nombreOb='El viejo guitarrista ciego')
    datos={
        'guit': guit
    }
    return render(request,'core/guitarrista.html',datos)

def habitacion(request):
    habi=Obra.objects.get(nombreOb='La Habitaci??n de Vincent en ??rles')
    datos={
        'habi': habi
    }
    return render(request,'core/habitacion.html',datos)

def hissam(request):
    his=Obra.objects.get(nombreOb='Hissam II')
    datos={
        'his': his
    }
    return render(request,'core/hissam.html',datos)

def hombrevitruvio(request):
    homb=Obra.objects.get(nombreOb='Hombre de Vitruvio')
    datos={
        'homb': homb
    }
    return render(request,'core/hombrevitruvio.html',datos)

def impresion(request):
    imp=Obra.objects.get(nombreOb='Impresi??n, sol naciente')
    datos={
        'imp': imp
    }
    return render(request,'core/impresion.html',datos)

def interchange(request):
    inter=Obra.objects.get(nombreOb='Interchange')
    datos={
        'inter': inter
    }
    return render(request,'core/interchange.html',datos)

def jardin(request):
    jard=Obra.objects.get(nombreOb='El jard??n del artista en Giverny')
    datos={
        'jard': jard
    }
    return render(request,'core/jardin.html',datos)

def judia(request):
    judi=Obra.objects.get(nombreOb='La novia jud??a')
    datos={
        'judi': judi
    }
    return render(request,'core/judia.html',datos)

def lafuente(request):
    lafu=Obra.objects.get(nombreOb='La Fuente')
    datos={
        'lafu': lafu
    }
    return render(request,'core/lafuente.html',datos)

def leccion(request):
    lecc=Obra.objects.get(nombreOb='Lecci??n de anatom??a del Dr. Nicolaes Tulp')
    datos={
        'lecc': lecc
    }
    return render(request,'core/leccion.html',datos)

def lirios(request):
    liri=Obra.objects.get(nombreOb='Lirios')
    datos={
        'liri': liri
    }
    return render(request,'core/lirios.html',datos)

def mascara(request):
    masca=Obra.objects.get(nombreOb='Mascara funeraria Lambayeque')
    datos={
        'masca': masca
    }
    return render(request,'core/mascara.html',datos)

def memoria(request):
    memo=Obra.objects.get(nombreOb='La persistencia de la memoria')
    datos={
        'memo': memo
    }
    return render(request,'core/memoria.html',datos)

def metamorfosis(request):
    meta=Obra.objects.get(nombreOb='Metamorfosis de Narciso')
    datos={
        'meta': meta
    }
    return render(request,'core/metamorfosis.html',datos)

def moises(request):
    moises=Obra.objects.get(nombreOb='El Mois??s')
    datos={
        'moises': moises
    }
    return render(request,'core/moises.html',datos)

def monalisa(request):
    mona=Obra.objects.get(nombreOb='La Mona Lisa')
    datos={
        'mona': mona
    }
    return render(request,'core/monalisa.html',datos)

def mujerespejo(request):
    chica=Obra.objects.get(nombreOb='Chica frente a un espejo')
    datos={
        'chica': chica
    }
    return render(request,'core/mujerespejo.html',datos)

def mujerllorando(request):
    mujer=Obra.objects.get(nombreOb='La mujer que llora')
    datos={
        'mujer': mujer
    }
    return render(request,'core/mujerllorando.html',datos)

def nocheestrellada(request):
    noche=Obra.objects.get(nombreOb='La Noche Estrellada')
    datos={
        'noche': noche
    }
    return render(request,'core/nocheestrellada.html',datos)

def nude(request):
    nude=Obra.objects.get(nombreOb='Nude with Joyous Painting')
    datos={
        'nude': nude
    }
    return render(request,'core/nude.html',datos)

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
    pai=Obra.objects.get(nombreOb='Paisaje en L???Estaque')
    datos={
        'pai': pai
    }
    return render(request,'core/paisaje.html',datos)

def pensador(request):
    pen=Obra.objects.get(nombreOb='El Pensador')
    datos={
        'pen': pen
    }
    return render(request,'core/pensador.html',datos)

def rabbit(request):
    rab=Obra.objects.get(nombreOb='Rabbit')
    datos={
        'rab': rab
    }
    return render(request,'core/rabbit.html',datos)

def registrarse(request):
    datos={'form' : UsuarioForm}
    if request.method=='POST':
        formulario=UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Registrado Correctamente")
            return redirect(to="inicarSesion")
    return render(request,'core/registrarse.html',datos)

def retorno(request):
    reto=Obra.objects.get(nombreOb='El retorno del hijo pr??digo')
    datos={
        'reto': reto
    }
    return render(request,'core/retorno.html',datos)

def retrato(request):
    retra=Obra.objects.get(nombreOb='Retrato de Pablo Picasso')
    datos={
        'retra': retra
    }
    return render(request,'core/retrato.html',datos)

def ronda(request):
    ronda=Obra.objects.get(nombreOb='La ronda de anoche')
    datos={
        'ronda': ronda
    }
    return render(request,'core/ronda.html',datos)

def ruedadebicicleta(request):
    rueda=Obra.objects.get(nombreOb='Una y Tres Sillas')
    datos={
        'rueda': rueda
    }
    return render(request,'core/ruedadebicicleta.html',datos)

def salvatormundi(request):
    salva=Obra.objects.get(nombreOb='Salvator Mundi')
    datos={
        'salva': salva
    }
    return render(request,'core/salvatormundi.html',datos)

def se??oras(request):
    se??oras=Obra.objects.get(nombreOb='Las se??oritas de Avignon')
    datos={
        'se??oras': se??oras
    }
    return render(request,'core/se??oras.html',datos)

def silla(request):
    silla=Obra.objects.get(nombreOb='Silla Cubierta de Grasa')
    datos={
        'silla': silla
    }
    return render(request,'core/silla.html',datos)

def sindicato(request):
    sindi=Obra.objects.get(nombreOb='Los s??ndicos de los pa??eros')
    datos={
        'sindi': sindi
    }
    return render(request,'core/sindicato.html',datos)

def sombrilla(request):
    somb=Obra.objects.get(nombreOb='Mujer con sombrilla')
    datos={
        'somb': somb
    }
    return render(request,'core/sombrilla.html',datos)

def soporte(request):
    return render(request,'core/soporte.html')

def sue??o(request):
    sue=Obra.objects.get(nombreOb='El sue??o')
    datos={
        'sue': sue
    }
    return render(request,'core/sue??o.html',datos)

def telefono(request):
    tele=Obra.objects.get(nombreOb='Tel??fono Langosta')
    datos={
        'tele': tele
    }
    return render(request,'core/telefono.html',datos)

def tentacion(request):
    tenta=Obra.objects.get(nombreOb='La tentaci??n de San Antonio')
    datos={
        'tenta': tenta
    }
    return render(request,'core/tentacion.html',datos)

def terraza(request):
    terra=Obra.objects.get(nombreOb='Terraza de Caf?? por la Noche')
    datos={
        'terra': terra
    }
    return render(request,'core/terraza.html',datos)

def tesoro(request):
    teso=Obra.objects.get(nombreOb='Tr??sor de Conques')
    datos={
        'teso': teso
    }
    return render(request,'core/tesoro.html',datos)

def tipoobras(request):
    return render(request,'core/tipoobras.html')

def tormenta(request):
    tor=Obra.objects.get(nombreOb='La tormenta en el mar de Galilea')
    datos={
        'tor': tor
    }
    return render(request,'core/tormenta.html',datos)

def trigal(request):
    tri=Obra.objects.get(nombreOb='Trigal con Cuervos')
    datos={
        'tri': tri
    }
    return render(request,'core/trigal.html',datos)

def ultimacena(request):
    cena=Obra.objects.get(nombreOb='La Ultima Cena')
    datos={
        'cena': cena
    }
    return render(request,'core/ultimacena.html',datos)

def unaytressillas(request):
    unay=Obra.objects.get(nombreOb='Una y Tres Sillas')
    datos={
        'unay': unay
    }
    return render(request,'core/unaytressillas.html',datos)

def unroble(request):
    roble=Obra.objects.get(nombreOb='Un Roble (An Oak Tree)')
    datos={
        'roble': roble
    }
    return render(request,'core/unroble.html',datos)

def ventana(request):
    vent=Obra.objects.get(nombreOb='La Ventana Abierta')
    datos={
        'vent': vent
    }
    return render(request,'core/ventana.html',datos)

def ventanas(request):
    ventanas=Obra.objects.get(nombreOb='Ventanas Simult??neas')
    datos={
        'ventanas': ventanas
    }
    return render(request,'core/ventanas.html',datos)

def venus(request):
    venus=Obra.objects.get(nombreOb='Venus de Milo')
    datos={
        'venus': venus
    }
    return render(request,'core/venus.html',datos)

def visigodo(request):
    visi=Obra.objects.get(nombreOb='Friso Visigodo')
    datos={
        'visi': visi
    }
    return render(request,'core/visigodo.html',datos)

def vives(request):
    vives=Obra.objects.get(nombreOb='Tiraz de Hixen o Hisam')
    datos={
        'vives': vives
    }
    return render(request,'core/vives.html',datos)