#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    // for (const character of characters) {
    //   request(character, function (error, response, body) {
    //     if (error) {
    //       console.log(error);
    //     } else {
    //       console.log(JSON.parse(body).name);
    //     }
    //   });
    // }
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
