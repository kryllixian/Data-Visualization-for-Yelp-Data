const express = require('express');
const hbs = require('hbs');
const fs = require('fs');
const url = require('url');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const model = require('./model.js')


// Configurate the connection to MySQL
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'yelp_data_new'
});
connection.connect();


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


// Set body parser
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());


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

app.get('/restaurants_recommendation', (req, res) => {
    res.render('restaurants_recommendation.hbs', {
        pageTitle: 'Restaurants Recommendation',
        currentYear: new Date().getFullYear()
    });
});

app.post('/restaurants_recommendation', (req, res) => {
    model.recommendation(connection, req, res, function(result) {
        console.log(req.body);
        // console.log(result);
        if (!result) {
            res.render('restaurants_recommendation.hbs', {
                pageTitle: 'Restaurants Recommendation',
                currentYear: new Date().getFullYear(),
                messages: JSON.stringify(result.messages, undefined, 2),
                restaurants: JSON.stringify(result.restaurants, undefined, 2),
                former_query: JSON.stringify(req.body, undefined, 2)
            });
        } else {
            res.render('restaurants_recommendation.hbs', {
                pageTitle: 'Restaurants Recommendation',
                currentYear: new Date().getFullYear(),
                messages: JSON.stringify(result.messages, undefined, 2),
                restaurants: JSON.stringify(result.restaurants, undefined, 2),
                former_query: JSON.stringify(req.body, undefined, 2)
            });
        }
    });
});

app.get('/pittsburgh', (req, res) => {
  var query = url.parse(req.url, true).query;
  if (JSON.stringify(query) != '{}') {
      var wordcloudName = query.wordcloud_name;
      switch (wordcloudName) {
          case 'restaurants':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Restaurants @ Pittsburgh',
                wordcloudTitle: 'RESTAURANTS',
                wordcloudSRC: '//cdn.tagul.com/json/e0bk9q14whez',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'shopping':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Shopping @ Pittsburgh',
                wordcloudTitle: 'SHOPPING',
                wordcloudSRC: '//cdn.tagul.com/json/d2o3sgc0zjs4',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'food':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Foods @ Pittsburgh',
                wordcloudTitle: 'FOODS',
                wordcloudSRC: '//cdn.tagul.com/json/pjljugdq8p8g',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'beauty_spas':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Beauty & Spas @ Pittsburgh',
                wordcloudTitle: 'BEAUTY & SPAS',
                wordcloudSRC: '//cdn.tagul.com/json/5qbyq1ttkys3',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'home_services':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Home Services @ Pittsburgh',
                wordcloudTitle: 'HOME SERVICES',
                wordcloudSRC: '//cdn.tagul.com/json/jvvdxbu81wa9',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'nightlife':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Nightlife @ Pittsburgh',
                wordcloudTitle: 'Nightlife',
                wordcloudSRC: '//cdn.tagul.com/json/roqx1mgemr7g',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'health_medical':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Health & Medical @ Pittsburgh',
                wordcloudTitle: 'HEALTH & MEDICAL',
                wordcloudSRC: '//cdn.tagul.com/json/t1m51ar0oa4d',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'bars':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Bars @ Pittsburgh',
                wordcloudTitle: 'BARS',
                wordcloudSRC: '//cdn.tagul.com/json/geprp19m8sxo',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'automotive':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Automotive @ Pittsburgh',
                wordcloudTitle: 'AUTOMOTIVE',
                wordcloudSRC: '//cdn.tagul.com/json/6hkzh64pystc',
                currentYear: new Date().getFullYear()
              });
              break;
          case 'local_services':
              res.render('wordcloud.hbs', {
                pageTitle: 'Wordcloud of Local Services @ Pittsburgh',
                wordcloudTitle: 'LOCAL SERVICES',
                wordcloudSRC: '//cdn.tagul.com/json/hc4efncpgfi2',
                currentYear: new Date().getFullYear()
              });
              break;
      }
  } else {
      res.render('pittsburgh.hbs', {
        pageTitle: 'Pittsburgh',
        currentYear: new Date().getFullYear()
      });
  }
});
// app.get('/wordcloud', (req, res) => {
//     res.render('wordcloud.hbs', {
//       pageTitle: 'Wordcloud of Restaurants @ Pittsburgh',
//       wordcloudTitle: 'RESTAURANTS',
//       wordcloudSRC: '//cdn.tagul.com/json/e0bk9q14whez',
//       currentYear: new Date().getFullYear()
//     });
// });


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
