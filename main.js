const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
const region = document.getElementById('region');
const ciudad = document.getElementById('ciudad');
const codpostal = document.getElementById('codpostal');
const direccion = document.getElementById('direccion');
const casadepto = document.getElementById('casadepto');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	
	
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const regionValue = region.value.trim();
	const ciudadValue = ciudad.value.trim();
	const codpostalValue = codpostal.value.trim();
	const direccionValue = direccion.value.trim();
	const casadeptoValue = casadepto.value.trim();



	if(emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'El formato del email debe ser: ejemplo@gmail.com');
	} else {
		setSuccessFor(email);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Ingrese una contraseña');
	} else if (!isPassword(passwordValue)) {
		setErrorFor(password, 'Debe tener 8 o más caracteres y una mayúscula' );
		
	}else{
		setSuccessFor(password);
	}

    if(regionValue === '') {
		setErrorFor(region, 'Ingrese su región de residencia.');
	} else {
		setSuccessFor(region);
	}

    if(ciudadValue === '') {
		setErrorFor(ciudad, 'Ingrese su ciudad de residencia.');
	} else {
		setSuccessFor(ciudad);
	}
	
    if(codpostalValue === '') {
		setErrorFor(codpostal, 'Ingrese un código postal.');
	} else {
		setSuccessFor(codpostal);
	}

	if(direccionValue === '') {
		setErrorFor(direccion, 'Ingrese su dirección.');
	} else {
		setSuccessFor(direccion);
	}

	if(casadeptoValue === '') {
		setErrorFor(casadepto, 'Ingrese su dirección.');
	} else {
		setSuccessFor(casadepto);
	}
	
	
	
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function isPassword(password) {
	return /^(?=\w*[A-Z])\S{8,16}$/.test(password);
}




