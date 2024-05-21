#!/usr/bin/node

const args = process.argv;
const filepath = args[2];

const fs = require('fs');

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
