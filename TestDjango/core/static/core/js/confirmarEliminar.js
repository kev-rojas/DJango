function confiEliminar()
{
    var respuesta = confirm("¿Estas seguro que deseas eliminar al usuario?");

    if (respuesta == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}