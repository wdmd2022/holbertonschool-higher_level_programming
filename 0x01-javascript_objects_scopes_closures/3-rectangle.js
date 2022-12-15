#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringy = '';
    for (let i = 0; i < this.width; i++) {
      stringy = stringy + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(stringy);
    }
  }
}
module.exports = Rectangle;
