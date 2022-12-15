#!/usr/bin/node
exports.converter = function (base) {
  return function changeMe (number) {
    return number.toString(base);
  };
};
