#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) console.log(err);
  const completed = {};
  const todos = JSON.parse(body);
  todos.forEach((element) => {
    if (element.completed && completed[element.userId] === undefined) {
      completed[element.userId] = 1;
    } else if (element.completed) {
      completed[element.userId] += 1;
    }
  });
  console.log(completed);
});
