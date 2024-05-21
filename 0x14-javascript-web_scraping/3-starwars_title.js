#!/usr/bin/node

/** Makes a request to a star-wars API and displays the title of
    a movie with a given episode number **/

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episodeNum = process.argv[2];

request(url + episodeNum, (err, resp, body) => {
  if (!err) {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
