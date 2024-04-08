#!/usr/bin/node

const argToNum = parseInt(process.argv[2]);

if (!argToNum) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < argToNum; i++) {
    console.log('C is fun');
  }
}
