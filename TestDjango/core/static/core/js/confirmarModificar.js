function eliminarUsuario(id){
    Swal.fire({
        "title": "¿Estas Seguro?",
        "text": "Esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton": true,
        "reverseButtons": true
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/del_usuario/"+id+"/"
        }
    }) 
}