#!/usr/bin/node
const fs = require('fs');
const fileTarget = process.argv[2];
const writeNow = process.argv[3];
fs.writeFile(fileTarget, writeNow, 'utf-8', function (error, content) {
  if (error) {
    console.error(error);
  }
});
