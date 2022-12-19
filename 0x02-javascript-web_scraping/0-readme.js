#!/usr/bin/node
const filestream = require('fs');
filestream.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
