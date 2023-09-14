#!/usr/bin/node
const numbArg = process.argv.slice(2).length;
if (numbArg === 0) {
  console.log('No argument');
} else if (numbArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
