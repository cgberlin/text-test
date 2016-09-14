

$('#bomb-mason').on('click', function(){
  $.get(
    '/mason',
    {'att', '4242234443', 'test'},
    console.log('success') 
  );
});
