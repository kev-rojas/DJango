$(document).ready(function() {
    //alert('paso1')
    //const url = "http://127.0.0.1:8000/api/lista_usua"
    //fetch(url)
    $.getJSON('http://127.0.0.1:8000/api/lista_usua', function(data) {
        console.log(data)
        var Usuario = data;        
        $('#nombre').html(Usuario.nombre);
        $('#email').html(Usuario.email);
        $('#contraseña').html(Usuario.contraseña);
    }).fail(function() {
        console.log('Error al consumir la API!');
    });
});