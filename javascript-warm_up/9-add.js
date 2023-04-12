#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
if (x && y) {
  const sum = add(x, y);
  console.log(sum);
} else {
  console.log('NaN');
}
