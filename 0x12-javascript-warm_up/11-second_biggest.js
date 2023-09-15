#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  let big = process.argv[2];
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > big) {
      big = process.argv[i];
    }
  }
  console.log(big);
}
