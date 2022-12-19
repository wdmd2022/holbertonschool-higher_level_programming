#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resultJSON = JSON.parse(body).results;
    let i = 0;
    for (const film in resultJSON) {
      const cast = resultJSON[film].characters;
      for (const person in cast) {
        if (cast[person].includes('/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
