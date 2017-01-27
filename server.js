const express = require('express');
const hbs = require('hbs');
const fs = require('fs');


var app = express();
const port = 3000;


// Configuration
hbs.registerPartials(__dirname + '/views/partials')
app.set('view engine', 'hbs');
app.use(express.static(__dirname + '/public'));


// Middleware
app.use((req, res, next) => {
  var now = new Date().toString();
  var log = `${now}: ${req.method} ${req.url}`;

  console.log(log);
  fs.appendFile('server.log', log + '\n', (err) => {
    if (err) {
      console.log('Unable to append to file system');
    }
  });
  next();
});


// app.get('/', (req, res) => {
//   // res.send('Hello Express!');
//   res.send({
//     name: 'Hao Wang',
//     likes: [
//       'Biking',
//       'Cities'
//     ]
//   });
// });


app.get('/statistics', (req, res) => {
  res.render('statistics.hbs', {
    pageTitle: 'Statistics',
    currentYear: new Date().getFullYear()
  });
});


app.get('/about', (req, res) => {
  res.render('about.hbs', {
    pageTitle: 'About',
    currentYear: new Date().getFullYear()
  });
});


app.get('/bad', (req, res) => {
  res.send({errorMessage: 'Unable to handle the request'});
});


app.listen(port);
console.log(`Starting server at localhost:${port}`);
