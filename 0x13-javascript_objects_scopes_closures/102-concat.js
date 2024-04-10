#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
let txtBuffer;

fs.readFile('./' + args[2], (err, data) => {
  if (err) throw err;
  txtBuffer = data.toString();
});

fs.readFile('./' + args[3], (err, data) => {
  if (err) throw err;
  txtBuffer += data.toString();
  fs.writeFile('./' + args[4], txtBuffer, (err) => {
    if (err) throw err;
  });
});
