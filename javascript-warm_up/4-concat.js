#!/usr/bin/node

if (process.argv[2] != null && process.argv[3] == null) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else if (process.argv[2] != null && process.argv[3] != null) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
}
