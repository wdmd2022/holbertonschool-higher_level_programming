#!/usr/bin/node
const request = require('request');
const target = process.argv[2];
request(target, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
