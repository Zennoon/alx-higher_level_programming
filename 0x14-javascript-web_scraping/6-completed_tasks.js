#!/usr/bin/node

/** Retrieves tasks data from an API and computes the number
    of tasks completed by user_id **/

const request = require('request');

const apiURL = process.argv[2];

request(apiURL, (err, res, body) => {
  const tasks = JSON.parse(body);
  const completedTasks = tasks.filter((task) => task.completed === true);
  const tasksById = {};

  if (err) {
    console.log(err);
  }
  for (const task of completedTasks) {
    if (task.userId in tasksById) {
      tasksById[task.userId] += 1;
    } else {
      tasksById[task.userId] = 1;
    }
  }
  console.log(tasksById);
});
