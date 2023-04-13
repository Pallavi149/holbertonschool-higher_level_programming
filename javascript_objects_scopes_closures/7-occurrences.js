#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for(var element of list) {
    if(element == searchElement) {
      total++;
    }
  }
  return total;
}
