function confiEliminar()
{
    var respuesta = confirm("¿Estas seguro que deseas eliminar al usuario?");

    if (respuesta == true)
    {
        var respuesta = alert("Usuario Eliminado")
        return true;
    }
    else
    {
        return false;
    }
}