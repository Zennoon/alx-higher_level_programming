/*
 Uses JQuery to fetch data from an API also using a variable query string and
 display it in an element when a button is pressed
*/

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const langCode = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, (res) => {
      $('DIV#hello').text(res.hello);
    });
  });
});
