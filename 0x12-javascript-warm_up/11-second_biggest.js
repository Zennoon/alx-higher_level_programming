#!/usr/bin/node

const numArgs = [];
let secondBiggest = 0;

for (let i = 2; i < process.argv.length; i++) {
  numArgs.push(parseInt(process.argv[i]));
}

numArgs.sort((a, b) => (a - b));
numArgs.reverse();
console.log(numArgs);
if (numArgs[1]) {
  secondBiggest = numArgs[1];
}
console.log(secondBiggest)
