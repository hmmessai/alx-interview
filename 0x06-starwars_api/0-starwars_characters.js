#!/usr/bin/node
const request = require('request');

if (process.argv.length < 4) {
  const movieId = process.argv[2];
  let url = 'https://swapi-api.alx-tools.com/api/films/';

  if (movieId) {
    url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
  }

  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const characters = JSON.parse(body).characters;
    const charactersName = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, resp, bod) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(bod).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
