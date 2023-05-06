$("#colaborador-form").validate({
    rules: {
        nombre:{
            required: true
        },
        apellido:{
            required: true
        },
        correo:{
            required: true,
            email: true
        },
        region:{
            required: true
        },
        ciudad: {
            required: true
        },
        cpostal: {
            required: true,
            number: true,
            minlength: 7,
            maxlength: 7
        },
        direccion: {
            required: true
        },
        direccion2: {
            required: true
        }
    },
    messages:{
        nombre:{
            required: "Ingrese su nombre"
        },
        apellido:{
            required: "Ingrese su apellido"
        },
        correo:{
            required: "Ingrese un correo electrónico.",
            email: "Ingrese un correo válido."
        },
        region:{
            required: "Seleccione una región."
        },
        ciudad:{
            required: "Ingrese una ciudad."
        },
        cpostal:{
            required: "Ingrese un código postal.",
            minlength: "El código postal debe tener 7 dígitos",
            maxlength: "El código postal debe tener 7 dígitos"
        },
        direccion: {
            required: "Ingrese su dirección."
        },
        direccion2: {
            required: "Ingrese un número de casa o departamento. Si no posee ingrese S/N."
        }
    }
})

$("#registrarme").click(function(){
    if($("#colaborador-form").valid() == false) {
        return;
    }
    let nombre = $("inputNombre").val()
    let apellido = $("inputApellido").val()
    let correo = $("inputEmail4").val()
    let region = $("inputState").val()
    let ciudad = $("inputCity").val()
    let cpostal = $("inputZip").val()
    let direccion = $("inputAddress").val()
    let direccion2 = $("inputAddress2").val()
})

