$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (funky) {
  $('#character').text(funky.name);
});
