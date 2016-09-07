var $ = require('jquery');

$('#bomb-mason').on('click', function(){
  $.get('/mason');
});
