#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) console.log(err);
  let count = 0;
  const movies = JSON.parse(body).results;
  for (const i in movies) {
    for (const characters in movies[i].characters) {
      let character = movies[i].characters[characters];
      character = character.split('/');
      if (character[character.length - 2] === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
