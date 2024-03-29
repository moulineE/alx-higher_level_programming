#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (err) console.log(err);
  const chars = JSON.parse(body).characters;
  for (let i = 0; i < chars.length; ++i) {
    setTimeout(() => {
      request(chars[i], function (err, res, body) {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
      }, 2000);
    });
  }
});
