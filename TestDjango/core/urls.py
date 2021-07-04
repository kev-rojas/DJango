from django.urls import path
from .views import consumeapi, consumeapi2, lista_usuarios, mod_usuario, del_usuario
from django.conf import settings
from django.conf.urls.static import static


from .views import inicio
from .views import artistas
from .views import tipoobras
from .views import inicarSesion
from .views import almuerzo
from .views import balloon
from .views import cap
from .views import capital
from .views import cases
from .views import chaosn2
from .views import cisnes
from .views import comedores
from .views import conceptos
from .views import coquelicots
from .views import corona
from .views import crepusculo
from .views import cristo
from .views import cuadron19
from .views import damaarmiño
from .views import discobolo
from .views import elfantes
from .views import elvacio
from .views import frescos
from .views import ginebra
from .views import guernica
from .views import guitarrista
from .views import habitacion
from .views import hissam
from .views import hombrevitruvio
from .views import impresion
from .views import interchange
from .views import jardin
from .views import judia
from .views import lafuente
from .views import leccion
from .views import lirios
from .views import mascara
from .views import memoria
from .views import metamorfosis
from .views import moises
from .views import monalisa
from .views import mujerespejo
from .views import mujerllorando
from .views import nocheestrellada
from .views import nude
from .views import obrasclaude
from .views import obrasdali
from .views import obrasleonardo
from .views import obraspablo
from .views import obrasrembrant
from .views import obrasvincent
from .views import pagartabs
from .views import pagartconc
from .views import pagartcont
from .views import pagartcub
from .views import pagesculturas
from .views import pagorfebreria
from .views import pagpinturas
from .views import pagtejidos
from .views import paisaje
from .views import pensador
from .views import rabbit
from .views import registrarse
from .views import retorno
from .views import retrato
from .views import ronda
from .views import ruedadebicicleta
from .views import salvatormundi
from .views import señoras
from .views import silla
from .views import sindicato
from .views import sombrilla
from .views import soporte
from .views import sueño
from .views import telefono
from .views import tentacion
from .views import terraza
from .views import tesoro
from .views import tormenta
from .views import trigal
from .views import ultimacena
from .views import unaytressillas
from .views import unroble
from .views import ventana
from .views import ventanas
from .views import venus
from .views import visigodo
from .views import vives

urlpatterns=[
    path('',inicio,name="inicio"),
    path('lista_usuarios',lista_usuarios,name="lista_usuarios"),
    path('mod_usuario/<id>',mod_usuario,name="mod_usuario"),
    path('del_usuario/<id>',del_usuario,name="del_usuario"),
    path('consumeapi', consumeapi, name="consumeapi"),
    path('consumeapi2', consumeapi2, name="consumeapi2"),
    #-----------------------------------------------------------------------------
    path('artistas',artistas,name="artistas"),
    path('tipoobras', tipoobras,name="tipoobras"),
    path('inicarSesion',inicarSesion,name="inicarSesion"),
    path('almuerzo',almuerzo,name="almuerzo"),
    path('balloon',balloon,name="balloon"),
    path('cap',cap,name="cap"),
    path('capital',capital,name="capital"),
    path('cases',cases,name="cases"),
    path('chaosn2',chaosn2,name="chaosn2"),
    path('cisnes',cisnes,name="cisnes"),
    path('comedores',comedores,name="comedores"),
    path('conceptos',conceptos,name="conceptos"),
    path('coquelicots',coquelicots,name="coquelicots"),
    path('corona',corona,name="corona"),
    path('crepusculo',crepusculo,name="crepusculo"),
    path('cristo',cristo,name="cristo"),
    path('cuadron19',cuadron19,name="cuadron19"),
    path('damaarmiño',damaarmiño,name="damaarmiño"),
    path('discobolo',discobolo,name="discobolo"),
    path('elfantes',elfantes,name="elfantes"),
    path('elvacio',elvacio,name="elvacio"),
    path('frescos',frescos,name="frescos"),
    path('ginebra',ginebra,name="ginebra"),
    path('guernica',guernica,name="guernica"),
    path('guitarrista',guitarrista,name="guitarrista"),
    path('habitacion',habitacion,name="habitacion"),
    path('hissam',hissam,name="hissam"),
    path('hombrevitruvio',hombrevitruvio,name="hombrevitruvio"),
    path('impresion',impresion,name="impresion"),
    path('interchange',interchange,name="interchange"),
    path('jardin',jardin,name="jardin"),
    path('judia',judia,name="judia"),
    path('lafuente',lafuente,name="lafuente"),
    path('leccion',leccion,name="leccion"),
    path('lirios',lirios,name="lirios"),
    path('mascara',mascara,name="mascara"),
    path('memoria',memoria,name="memoria"),
    path('metamorfosis',metamorfosis,name="metamorfosis"),
    path('moises',moises,name="moises"),
    path('monalisa',monalisa,name="monalisa"),
    path('mujerespejo',mujerespejo,name="mujerespejo"),
    path('mujerllorando',mujerllorando,name="mujerllorando"),
    path('nocheestrellada',nocheestrellada,name="nocheestrellada"),
    path('nude',nude,name="nude"),
    path('obrasclaude',obrasclaude,name="obrasclaude"),
    path('obrasdali',obrasdali,name="obrasdali"),
    path('obrasleonardo',obrasleonardo,name="obrasleonardo"),
    path('obraspablo',obraspablo,name="obraspablo"),
    path('obrasrembrant',obrasrembrant,name="obrasrembrant"),
    path('obrasvincent',obrasvincent,name="obrasvincent"),
    path('pagartabs',pagartabs,name="pagartabs"),
    path('pagartconc',pagartconc,name="pagartconc"),
    path('pagartcont',pagartcont,name="pagartcont"),
    path('pagartcub',pagartcub,name="pagartcub"),
    path('pagesculturas',pagesculturas,name="pagesculturas"),
    path('pagorfebreria',pagorfebreria,name="pagorfebreria"),
    path('pagpinturas',pagpinturas,name="pagpinturas"),
    path('pagtejidos',pagtejidos,name="pagtejidos"),
    path('paisaje',paisaje,name="paisaje"),
    path('pensador',pensador,name="pensador"),
    path('rabbit',rabbit,name="rabbit"),
    path('registrarse',registrarse,name="registrarse"),
    path('retorno',retorno,name="retorno"),
    path('retrato',retrato,name="retrato"),
    path('ronda',ronda,name="ronda"),
    path('ruedadebicicleta',ruedadebicicleta,name="ruedadebicicleta"),
    path('salvatormundi',salvatormundi,name="salvatormundi"),
    path('señoras',señoras,name="señoras"),
    path('silla',silla,name="silla"),
    path('sindicato',sindicato,name="sindicato"),
    path('sombrilla',sombrilla,name="sombrilla"),
    path('soporte',soporte,name="soporte"),
    path('sueño',sueño,name="sueño"),
    path('telefono',telefono,name="telefono"),
    path('tentacion',tentacion,name="tentacion"),
    path('terraza',terraza,name="terraza"),
    path('tesoro',tesoro,name="tesoro"),
    path('tipoobras',tipoobras,name="tipoobras"),
    path('tormenta',tormenta,name="tormenta"),
    path('trigal',trigal,name="trigal"),
    path('ultimacena',ultimacena,name="ultimacena"),
    path('unaytressillas',unaytressillas,name="unaytressillas"),
    path('unroble',unroble,name="unroble"),
    path('ventana',ventana,name="ventana"),
    path('ventanas',ventanas,name="ventanas"),
    path('venus',venus,name="venus"),
    path('visigodo',visigodo,name="visigodo"),
    path('vives',vives,name="vives"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)