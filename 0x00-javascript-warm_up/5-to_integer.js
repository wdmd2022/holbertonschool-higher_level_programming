#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  const llCoolNum = parseInt(process.argv[2]);
  console.log('My number: ' + llCoolNum);
}
