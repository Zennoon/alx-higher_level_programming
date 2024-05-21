#!/usr/bin/node

/** Makes a request to a star-wars API and displays the number of movies
    the character 'Wedge Antilles' is present in **/

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';

request(url + 18, (err, resp, body) => {
  if (!err) {
    const character = JSON.parse(body);
    console.log(character.films.length);
  }
});
