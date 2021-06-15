function confiModificar()
{
    var respuesta = confirm("¿Estas seguro que deseas modificar al usuario?");

    if (respuesta == true)
    {
        var respuesta = alert("Usuario Modificado")
        return true;
    }
    else
    {
        return false;
    }
}