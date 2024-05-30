/*
 Triggers a function when the document's DOM is ready. The function makes a
 request using AJAX to an API and embeds some data to an element
*/

$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (res) => {
    $('DIV#hello').text(res.hello);
  });
});
