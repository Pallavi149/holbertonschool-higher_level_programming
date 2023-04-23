#!/usr/bin/node

const request =require('request');
const url = process.argv[2];
request(url, { json: true},(error, respose, body) => {
    if (error) {
      console.log(error);
    }
    const completedTasksByUser = {};
    body.forEach(task => {
	if (task.completed) {
	  if (completedTasksByUser[task.userId]) {
              completedTasksByUser[task.userId]++;
	  } else {
              completedTasksByUser[task.userId] = 1;
	  }
	}
    });
    console.log(completedTasksByUser);
});
