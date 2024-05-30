/*
 Adds a class to the header element when another element is clicked
 */

$('DIV#red_header').on('click', () => {
  $('header').addClass('red');
});
