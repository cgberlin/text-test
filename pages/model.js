

$('#bomb-mason').on('click', function(){
  data = {
    carrier : $('#carrier').val(),
    number : $('#number').val(),
    msg : $('#msg').val(),
    amount : $('#amount').val()
  };

  $.get( '/mason', data, function(){
    console.log('yas');
  });
});
