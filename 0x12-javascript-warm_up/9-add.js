#!/usr/bin/node

/*
 * adds its first two command line arguments and prints the result
 */

const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(add(firstArg, secondArg));

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
