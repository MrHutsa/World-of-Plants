
console.log("hola")
// Nombre Completo

const miInput = document.getElementById('nombre');

// Quita la validación mientras escribes
miInput.addEventListener('input', () => {
    // Quita el mensaje según escribes
    miInput.setCustomValidity('');
    // Comprueba si debe validarlo
    miInput.checkValidity();
});

// Muestra el mensaje de validación
miInput.addEventListener('invalid', () => {
    miInput.setCustomValidity('Si no es molesta... ¿me dices tu nombre?');
});

// Nombre Usuario

// Variables
const inputUsuario = document.getElementById('usuario');
const mensajeErrorUsuarioCorto = "Muy corta. Dame un nombre con 4 o mas caracteres.";

// Eventos
inputUsuario.addEventListener('input', () => {
    // Quita el mensaje según escribes
    inputUsuario.setCustomValidity('');
    // Comprueba si debe validarlo
    inputUsuario.checkValidity();
});

inputUsuario.addEventListener('invalid', () => {
    inputUsuario.setCustomValidity(mensajeErrorUsuarioCorto);
});

// Email

const miEmail = document.getElementById('email');

// Quita la validación mientras escribes
miEmail.addEventListener('input', () => {
    // Quita el mensaje según escribes
    miEmail.setCustomValidity('');
    // Comprueba si debe validarlo
    miEmail.checkValidity();
});

// Muestra el mensaje de validación
miEmail.addEventListener('invalid', () => {
    miEmail.setCustomValidity('Me parece que esto no es un E-mail');
});

// Telefono

const miTelefono = document.getElementById('telefono');

// Quita la validación mientras escribes
miTelefono.addEventListener('input', () => {
    // Quita el mensaje según escribes
    miTelefono.setCustomValidity('');
    // Comprueba si debe validarlo
    miTelefono.checkValidity();
});

// Muestra el mensaje de validación
miTelefono.addEventListener('invalid', () => {
    miTelefono.setCustomValidity('No es un número');
});