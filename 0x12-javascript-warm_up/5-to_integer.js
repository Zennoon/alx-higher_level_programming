#!/usr/bin/node

const argToNum = parseInt(process.argv[2]);

if (argToNum) {
  console.log(`My number: ${argToNum}`);
} else {
  console.log('Not a number');
}
