const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Name >> ", (name) => {
  rl.question("Age >> ", (age) => {
    rl.question("Username >> ", (username) => {
      console.log(`Your name is ${name}, you are ${age} years old and your username is ${username}`);
    });
  });
});
