#!/usr/bin/node
const request = require('request');

if (process.argv.length < 4) {
const movie_id = process.argv[2]
let url = 'https://swapi-api.alx-tools.com/api/films/';

if (movie_id) {
  url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;
}

request(url, (error, response, body) => {
    if (error) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    for (character of characters) {
      request(character, (err, resp, bod) => {
	 if (err) {
	   console.log(err)
	 }
         let name = JSON.parse(bod).name;
	 console.log(name);
      })
    }
});
}
