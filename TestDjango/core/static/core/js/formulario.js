function validar(){
    var form = document.form;

    if(form.name.value==0){
        alert("El campo Nombre se encuentra vacio")
        form.name.value=="";
        
        
    }

    if(form.email.value==0){
        alert("El campo Correo Electronico se encuentra vacio")
        form.email.value=="";
        
    }

    if(form.password.value==0){
        alert("El campo Contraseña se encuentra vacio")
        form.password.value=="";
        
    }
    return false;
}
