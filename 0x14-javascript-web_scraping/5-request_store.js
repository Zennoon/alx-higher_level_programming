#!/usr/bin/node

/** Makes a request to an API endpoint and stores the response in a file **/

const fs = require('fs');
const request = require('request');

const apiURL = process.argv[2];
const filePath = process.argv[3];

request.get(apiURL).pipe(fs.createWriteStream(filePath));
