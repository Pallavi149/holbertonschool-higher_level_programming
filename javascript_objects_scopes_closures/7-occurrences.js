#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let element = 0; element < list.length; element++) {
    if (list[element] === searchElement) {
      total++;
    }
  }
  return total;
};
