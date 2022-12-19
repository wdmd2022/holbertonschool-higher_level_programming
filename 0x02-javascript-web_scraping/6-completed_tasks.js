#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const stuffDone = {};
    const tasksList = JSON.parse(body);
    for (let i = 0; i < tasksList.length; i++) {
      const userId = tasksList[i].userId;
      const whatDone = tasksList[i].completed;
      if (whatDone) {
        if (!stuffDone[userId]) {
          stuffDone[tasksList[i].userId] = 1;
        } else {
          stuffDone[tasksList[i].userId] += 1;
        }
      }
    }
    console.log(stuffDone);
  }
});
