$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const llCoolZult in data.results) {
    $('ul#list_movies').append(`<li>${data.results[llCoolZult].title}</li>`);
  }
});
