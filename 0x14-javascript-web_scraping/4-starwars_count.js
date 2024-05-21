#!/usr/bin/node

/** Makes a request to a star-wars API and displays the number of movies
    the character 'Wedge Antilles' is present in **/

const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (!err) {
    const films = JSON.parse(body).results;

    const filmsWithWedge = films.filter((film) => {
      let hasWedge = false;
      for (const character of film.characters) {
        if (character.endsWith('18/') || character.endsWith('18')) {
          hasWedge = true;
          break;
        }
      }
      return (hasWedge);
    });
    console.log(filmsWithWedge.length);
  }
});
