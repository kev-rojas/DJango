$(document).ready(function() {
    //alert('paso1')
    //const url = "http://127.0.0.1:8000/api/lista_usua"
    //fetch(url)
    $.getJSON('http://127.0.0.1:8000/api/listado_obra', function(data) {
        console.log(data)
        var Obra = data;        
        $('#obnombre').html(Obra.nombreOb);
        $('#obautor').html(Obra.autor);
        $('#obaño').html(Obra.año);
        $('#obtecnica').html(Obra.tecnica);
        $('#obtamaño').html(Obra.tamaño);
        $('#obimagen').html(Obra.imagen);
    }).fail(function() {
        console.log('Error al consumir la API!');
    });
});