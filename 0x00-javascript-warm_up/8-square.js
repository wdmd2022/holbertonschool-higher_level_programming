#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let stringy = '';
  for (let r = 0; r < parseInt(process.argv[2]); r++) {
    stringy = stringy + 'X';
  }
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(stringy);
  }
}
