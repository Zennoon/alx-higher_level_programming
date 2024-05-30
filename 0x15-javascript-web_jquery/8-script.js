/*
 Uses AJAX to make a GET request to a Star-Wars info API, and receives an object
 containing an array 'results' of the movies, the titles of which are appended
 to a list element as a list item
*/

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (res) => {
  res.results.forEach(movie => {
    $(`<li>${movie.title}</li>`).appendTo($('UL#list_movies'));
  });
});
