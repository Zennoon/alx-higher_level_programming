#!/usr/bin/node

/** Makes a request to a given URL and displays the status code **/

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, data) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});
