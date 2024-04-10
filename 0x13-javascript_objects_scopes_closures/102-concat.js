#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
let txtBuffer = '';

txtBuffer = fs.readFileSync('./' + args[2]).toString() +
    fs.readFileSync('./' + args[3]).toString();
fs.writeFileSync('./' + args[4], txtBuffer);
