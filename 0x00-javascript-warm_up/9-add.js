#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const i = parseInt(process.argv[2]);
const j = parseInt(process.argv[3]);
console.log(add(i, j));
