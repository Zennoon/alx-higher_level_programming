#!/usr/bin/node

/** Makes requests to a Star-Wars data API and displays the names of
    characters in a movie with a given movie ID **/

const request = require('request');

const apiURL = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

request(apiURL + movieID, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const characters = JSON.parse(body).characters;
  displayCharacterNames(characters);
});

async function displayCharacterNames (characters) {
  for (const character of characters) {
    const characterData = new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });
    await characterData.then((response) => {
      console.log(JSON.parse(response).name);
    });
  }
}
