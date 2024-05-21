#!/usr/bin/node

/** Writes given data to a given file **/

const args = process.argv;
const filepath = args[2];
const data = args[3];

const fs = require('fs');

fs.writeFile(filepath, data, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
