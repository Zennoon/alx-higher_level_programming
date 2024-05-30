/*
 Toggles classes 'red' and 'green' of the header element when another
 element is clicked
 */

$('DIV#toggle_header').on('click', () => {
  $('header').toggleClass('red');
  $('header').toggleClass('green');

  // Just in case the header starts off having both or neither classes
  if ($('header').hasClass('green') &&
      $('header').hasClass('red')) {
    $('header').removeClass('red');
  }
  if (!$('header').hasClass('green') &&
      !$('header').hasClass('red')) {
    $('header').addClass('green');
  }
});
