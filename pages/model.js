

$('#bomb-mason').on('click', function(){
  $.get(
    url: '/mason',    //your url eg. mypage.php
    data: ['att', '4242234443', 'test'],   // Parameter you want to pass eg. {version:"5" , language : "php"}
    success: console.log('success') // function after success
  );
});
