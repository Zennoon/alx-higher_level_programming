/*
 Makes an AJAX get request to a Star-Wars info API and uses the response to
 embed some value to an element
*/

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (res, stat) => {
  $('DIV#character').text(res.name);
});
