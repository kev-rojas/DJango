function confiModificar()
{
    var respuesta = confirm("¿Estas seguro que deseas modificar al usuario?");

    if (respuesta == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}