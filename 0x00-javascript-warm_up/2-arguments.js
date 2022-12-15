#!/usr/bin/node
const length = process.argv.length;
if (length === 2) {
  console.log('No argument');
}
if (length === 3) {
  console.log('Argument found');
}
if (length === 4) {
  console.log('Arguments found');
}
