#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
try {
  fs.writeFileSync(process.argv[2], data, { flag: 'a+' }); // 'a+' is append mode
} catch (err) {
  console.error(err);
}
