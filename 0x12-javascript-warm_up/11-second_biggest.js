#!/usr/bin/node

const numArgs = [];
let secondBiggest = 0;

for (let i = 2; i < process.argv.length; i++) {
  numArgs.push(process.argv[i]);
}

numArgs.sort();
numArgs.reverse();
if (numArgs[1]) {
  secondBiggest = numArgs[1];
}
console.log(secondBiggest)
