

$('#bomb-mason').on('click', function(){
  data = {
    carrier : 'att',
    number : '4242234443',
    msg : 'test'
  };

  $.get( '/mason', data, function(){
    console.log('yas');
  });
});
