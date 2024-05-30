/*
 Modifies the text of the header element when another element is clicked
*/

$('DIV#update_header').on('click', () => {
  $('header').text('New Header!!!');
});
