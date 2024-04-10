#!/usr/bin/node

const dict = require('./101-data').dict;
const sortedDict = {};

for (const item in dict) {
  if (sortedDict[dict[item]]) {
    sortedDict[dict[item]].push(item);
  } else {
    sortedDict[dict[item]] = [item];
  }
}

console.log(sortedDict);
