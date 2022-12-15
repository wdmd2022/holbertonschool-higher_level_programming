#!/usr/bin/node
exports.esrever = function (list) {
  const newCoolerList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newCoolerList.push(list[i]);
  }
  return newCoolerList;
};
