const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

$('#typeEmailX').blur(function() {
  const email = $(this).val();
  const emailInput = $(this);

  if (email === '') {
    if (!emailInput.hasClass('is-invalid')) {
      emailInput.addClass('is-invalid');
      emailInput.after('<div class="invalid-feedback">Debe ingresar su correo electrónico.</div>');
    }
  } else if (!regexEmail.test(email)) {
    if (!emailInput.hasClass('is-invalid')) {
      emailInput.addClass('is-invalid');
      emailInput.after('<div class="invalid-feedback">Debe ingresar un correo electrónico válido.</div>');
    }
  } else {
    emailInput.removeClass('is-invalid');
    const mensajeIntrusivo = $('#emailFeedback');
    mensajeIntrusivo.text('');
  }
});

$('#loginForm').submit(function(event) {
  event.preventDefault();

  const email = $('#typeEmailX').val();
  const password = $('#typePasswordX').val();

  if (email === '') {
    $('#typeEmailX').addClass('is-invalid');
    $('#emailFeedback').text('Debe ingresar su correo electrónico.');
  } else if (!regexEmail.test(email)) {
    $('#typeEmailX').addClass('is-invalid');
    $('#emailFeedback').text('Debe ingresar un correo electrónico válido.');
  } else {
    $('#typeEmailX').removeClass('is-invalid');
    $('#emailFeedback').text('');
  }

  if (password.length < 8) {
    $('#typePasswordX').addClass('is-invalid');
    $('#passwordFeedback').text('La contraseña debe tener al menos 8 caracteres.');
  } else {
    $('#typePasswordX').removeClass('is-invalid');
    $('#passwordFeedback').text('');
  }

  if (regexEmail.test(email) && password.length >= 8) {
    this.submit();
    window.location.href = "../index.html";
  }
});


