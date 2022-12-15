#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
  constructor () {
    super(size);
  }
  charPrint (c = 'X') {
    let stringy = '';
    for (let i = 0; i < this.width; i++) {
      stringy = stringy + c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(stringy);
    }
  }
}
