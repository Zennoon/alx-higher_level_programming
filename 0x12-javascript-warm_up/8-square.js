#!/usr/bin/node

/*
 * Prints a square of given size
 */

const givenSize = parseInt(process.argv[2]);

if (!givenSize) {
  console.log('Missing size');
} else {
  for (let i = 0; i < givenSize; i++) {
    console.log('X'.repeat(givenSize));
  }
}
