// Obtener los elementos del formulario
// Obtener referencia al formulario de registro
const registroForm = document.getElementById("registro-form");

// Agregar un controlador de eventos al formulario de registro
registroForm.addEventListener("submit", (event) => {
  // Prevenir el comportamiento por defecto del formulario
  event.preventDefault(); // Evita que el formulario se envíe

// Obtener los valores de los campos de entrada
const nombreInput = document.getElementById('nombre');
const usuarioInput = document.getElementById('usuario');
const emailInput = document.getElementById('email');
const telefonoInput = document.getElementById('telefono');
const contraseñaInput = document.getElementById('contraseña');
const confirmeContraseñaInput = document.getElementById('confirmeContraseña');

const nombre = nombreInput.value.trim();
const usuario = usuarioInput.value.trim();
const email = emailInput.value.trim();
const telefono = telefonoInput.value.trim();
const contraseña = contraseñaInput.value.trim();
const confirmeContraseña = confirmeContraseñaInput.value.trim();


// NOMBRE
if (nombre === '') {
  if (!nombreInput.classList.contains('error')) {
    nombreInput.classList.add('error');
    nombreInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar su nombre completo.</p>');
  }
} else {
  nombreInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#nombre + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}

// USUARIO
if (usuario === '') {
  if (!usuarioInput.classList.contains('error')) {
    usuarioInput.classList.add('error');
    usuarioInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar su nombre de usuario.</p>');
  }
} else {
  usuarioInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#usuario + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}

// EMAIL
const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if (email === '') {
  if (!emailInput.classList.contains('error')) {
    emailInput.classList.add('error');
    emailInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar su correo electrónico.</p>');
  }
} else if (!regexEmail.test(email)) { //la expresion test es para verificar si el email proporcionado coincide con el patron definido
  if (!emailInput.classList.contains('error')) {
    emailInput.classList.add('error');
    emailInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar un correo electrónico válido.</p>');
  }
} else {
  emailInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#email + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}

// TELEFONO
const regexTelefono = /^\d{3}\d{3}\d{3}$/;
if (telefono === '') {
  if (!telefonoInput.classList.contains('error')) {
    telefonoInput.classList.add('error');
    telefonoInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar su número de teléfono.</p>');
  }
} else if (!regexTelefono.test(telefono)) { //la expresion test es para verificar si el numero telefonico proporcionado coincide con el patron definido
  if (!telefonoInput.classList.contains('error')) {
    telefonoInput.classList.add('error');
    telefonoInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar un número de teléfono válido (Ej: 111-222-333).</p>');
  }
} else {
  telefonoInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#telefono + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}

// CONTRASEÑA
if (contraseña === '') {
  if (!contraseñaInput.classList.contains('error')) {
    contraseñaInput.classList.add('error');
    contraseñaInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Debe ingresar su contraseña.</p>');
  }
} else if (!validarContraseña(contraseña)) {
  if (!contraseñaInput.classList.contains('error')) {
    contraseñaInput.classList.add('error');
    contraseñaInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.</p>');
  }
} else {
  contraseñaInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#contraseña + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}


// CONFIRME CONTRASEÑA
if (confirmeContraseña === '') {
  if (!confirmeContraseñaInput.classList.contains('error')) {
    confirmeContraseñaInput.classList.add('error');
    confirmeContraseñaInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">Repita la contraseña.</p>');
  }
} else if (confirmeContraseña !== contraseña) {
  if (!confirmeContraseñaInput.classList.contains('error')) {
    confirmeContraseñaInput.classList.add('error');
    confirmeContraseñaInput.insertAdjacentHTML('afterend', '<p class="mensaje-intrusivo">La contraseña debe ser igual a la anterior.</p>');
  }
} else {
  confirmeContraseñaInput.classList.remove('error');
  const mensajeIntrusivo = document.querySelector('#confirmeContraseña + .mensaje-intrusivo');
  if (mensajeIntrusivo) {
    mensajeIntrusivo.remove();
  }
}

function validarContraseña(contraseña) {
  const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;
  return regex.test(contraseña);
}

// Verificar si todos los campos son válidos
const camposValidos = !nombreInput.classList.contains('error') && !usuarioInput.classList.contains('error') && !emailInput.classList.contains('error') && !telefonoInput.classList.contains('error') && !contraseñaInput.classList.contains('error') && !confirmeContraseñaInput.classList.contains('error');

if (camposValidos) {
  // Enviar el formulario y redireccionar a la página de inicio
  registroForm.submit();
  window.location.href = "../index.html";
}
});
