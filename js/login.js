// JQUERY



  $(document).ready(function() {
    $('button[type="submit"]').click(function() {
      var email = $('#typeEmailX').val();
      var password = $('#typePasswordX').val();
      if (email && password) {
        alert('Bienvenido, ' + email + '!');
      }
    });
  });
