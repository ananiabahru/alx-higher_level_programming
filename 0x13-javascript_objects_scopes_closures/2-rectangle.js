#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
}
module.exports = Rectangle;
