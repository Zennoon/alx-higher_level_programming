/*
 Add an event listener to when 'Enter' is pressed when focused in input field
*/

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const langCode = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, (res) => {
      $('DIV#hello').text(res.hello);
    });
  });

  $('INPUT#language_code').on('keypress', (event) => {
    if (event.key === 'Enter' || event.which === 13) {
      const langCode = $('INPUT#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, (res) => {
        $('DIV#hello').text(res.hello);
      });
    }
  });
});
