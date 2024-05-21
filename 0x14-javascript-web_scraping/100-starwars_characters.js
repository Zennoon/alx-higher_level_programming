#!/usr/bin/node

/** Makes a request to a Star-Wars data API and displays the names of
    characters in a movie with a given movie ID **/

const request = require('request');

const apiURL = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

request(apiURL + movieID, (err, resp, body) => {
  const film = JSON.parse(body);
  const characters = film.characters;

  if (err) {
    console.log(err);
  }
  for (const character of characters) {
    request(character, (err, resp, body) => {
      if (err) {
        console.log(err);
      }
      const curr = JSON.parse(body);
      console.log(curr.name);
    });
  }
});
