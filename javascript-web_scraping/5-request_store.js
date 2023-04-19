#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
// node 5-request_store.js http://loripsum.net/api loripsum
