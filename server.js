const express = require('express');
const hbs = require('hbs');
const fs = require('fs');
const url = require('url');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const model = require('./model.js');

const helper = require('./helper.js');

// Read data
var pittsburgh_restaurants_dic = {};
helper.getPittsburghRestaurantsData(function (result) {
    if (result.message != 'SUCCESS') {
        console.log(result.message);
    } else {
        pittsburgh_restaurants_dic = result.data;
        // console.log(result.data);
    }
});



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
                message: JSON.stringify(result.message, undefined, 2),
                restaurants: JSON.stringify(result.restaurants, undefined, 2),
                former_query: JSON.stringify(req.body, undefined, 2)
            });
        } else {
            // Generate key words for the query
            key_words = {};
            for (key in req.body) {
                if (key == 'Alcohol') {
                    key_words['alcohol'] = 1;
                    key_words['wine'] = 1;
                    key_words['beer'] = 1;
                    key_words['bar'] = 1;
                    key_words['pub'] = 1;
                    key_words['wine'] = 1;
                } else if (key.startsWith('Ambience_')) {
                    key_words['ambience'] = 1;
                    key_words['atmosphere'] = 1;
                    key_words['environment'] = 1;
                    key_words['casual'] = 1;
                    key_words['classy'] = 1;
                    key_words['gorgeous'] = 1;
                    key_words['fancy'] = 1;
                    key_words['divey'] = 1;
                    key_words['hipster'] = 1;
                    key_words['cool'] = 1;
                    key_words['sexy'] = 1;
                    key_words['divey'] = 1;
                    key_words['intimate'] = 1;
                    key_words['private'] = 1;
                    key_words['close'] = 1;
                    key_words['chamber'] = 1;
                    key_words['romantic'] = 1;
                    key_words['fantastic'] = 1;
                    key_words['amorous'] = 1;
                    key_words['touristy'] = 1;
                    key_words['trendy'] = 1;
                    key_words['famous'] = 1;
                    key_words['modern'] = 1;
                    key_words['beautiful'] = 1;
                    key_words['popular'] = 1;
                    key_words['fashionable'] = 1;
                    key_words['tony'] = 1;
                    key_words['upscale'] = 1;
                    key_words['superior'] = 1;
                    key_words['modern'] = 1;
                    key_words['amazing'] = 1;
                } else if (key.startsWith('DietaryRestrictions_')) {
                    key_words['dietary'] = 1;
                    key_words['restriction'] = 1;
                    key_words['restrictions'] = 1;
                    key_words['dairy-free'] = 1;
                    key_words['dairy'] = 1;
                    key_words['gluten-free'] = 1;
                    key_words['gluten'] = 1;
                    key_words['halal'] = 1;
                    key_words['hallal'] = 1;
                    key_words['kosher'] = 1;
                    key_words['soy-free'] = 1;
                    key_words['soy'] = 1;
                    key_words['vegan'] = 1;
                    key_words['vegetarian'] = 1;
                } else if (key.indexOf('Parking') != -1) {
                    key_words['park'] = 1;
                    key_words['parking'] = 1;
                    key_words['bike'] = 1;
                    key_words['bikes'] = 1;
                    key_words['bicycle'] = 1;
                    key_words['bicycles'] = 1;
                    key_words['garage'] = 1;
                    key_words['lot'] = 1;
                    key_words['street'] = 1;
                    key_words['valet'] = 1;
                    key_words['validate'] = 1;
                    key_words['validated'] = 1;
                } else if (key.startsWith('Music_')) {
                    key_words['music'] = 1;
                    key_words['song'] = 1;
                    key_words['songs'] = 1;
                    key_words['sound'] = 1;
                    key_words['audio'] = 1;
                    key_words['background'] = 1;
                    key_words['dj'] = 1;
                    key_words['jukebox'] = 1;
                    key_words['karaoke'] = 1;
                    key_words['live'] = 1;
                    key_words['video'] = 1;
                    key_words['dance'] = 1;
                    key_words['dancing'] = 1;
                } else if (key == 'NoiseLevel') {
                    key_words['quiet'] = 1;
                    key_words['comfortable'] = 1;
                    key_words['loud'] = 1;
                    key_words['noisy'] = 1;
                } else if (key == 'RestaurantsPriceRange2') {
                    key_words['price'] = 1;
                    key_words['cost'] = 1;
                } else if (key == 'RestaurantsAttire') {
                    key_words['casual'] = 1;
                    key_words['dressy'] = 1;
                    key_words['formal'] = 1;
                    key_words['official'] = 1;
                    key_words['leisure'] = 1;
                    key_words['informal'] = 1;
                } else if (key.startsWith('GoodForMeal_')) {
                    key_words['breakfast'] = 1;
                    key_words['brunch'] = 1;
                    key_words['lunch'] = 1;
                    key_words['dessert'] = 1;
                    key_words['dinner'] = 1;
                    key_words['late'] = 1;
                    key_words['night'] = 1;
                    key_words['evening'] = 1;
                    key_words['morning'] = 1;
                    key_words['noon'] = 1;
                    key_words['afternoon'] = 1;
                } else if (key.startsWith('BestNights_')) {
                    key_words['monday'] = 1;
                    key_words['tuesday'] = 1;
                    key_words['wednesday'] = 1;
                    key_words['thursday'] = 1;
                    key_words['friday'] = 1;
                    key_words['saturday'] = 1;
                    key_words['sunday'] = 1;
                } else if (key == 'GoodForKids') {
                    key_words['child'] = 1;
                    key_words['children'] = 1;
                    key_words['kid'] = 1;
                    key_words['kids'] = 1;
                } else if (key == 'HasTV') {
                    key_words['tv'] = 1;
                    key_words['television'] = 1;
                    key_words['screen'];
                } else if (key == 'OutdoorSeating') {
                    key_words['outdoor'] = 1;
                    key_words['outside'] = 1;
                } else if (key == 'WheelchairAccessible') {
                    key_words['wheel'] = 1;
                    key_words['chari'] = 1;
                    key_words['wheelchair'] = 1;
                } else if (key == 'WiFi') {
                    key_words['wifi'] = 1;
                    key_words['wi-fi'] = 1;
                } else if (key == 'Open24Hours') {
                    key_words['open'] = 1;
                    key_words['hour'] = 1;
                    key_words['hours'] = 1;
                    key_words['24'] = 1;
                } else if (key == 'Smoking') {
                    key_words['smoking'] = 1;
                    key_words['smoke'] = 1
                } else if (key == 'DogsAllowed') {
                    key_words['dog'] = 1;
                    key_words['dogs'] = 1;
                    key_words['pet'] = 1;
                    key_words['puppy'] = 1;
                } else if (key == 'DriveThru') {
                    key_words['drivethru'] = 1;
                    key_words['drive'] = 1;
                    key_words['drive-thru'] = 1;
                    key_words['thru'] = 1;
                } else if (key == 'ByAppointmentOnly' || key == 'RestaurantsReservations') {
                    key_words['appointment'] = 1;
                    key_words['appoint'] = 1;
                    key_words['reserve'] = 1;
                    key_words['reservation'] = 1;
                } else if (key == 'BusinessAcceptsCreditCards') {
                    key_words['credit'] = 1;
                    key_words['debit'] = 1;
                    key_words['card'] = 1;
                    key_words['cards'] = 1;
                } else if (key == 'RestaurantsDelivery') {
                    key_words['deliver'] = 1;
                    key_words['delivery'] = 1;
                } else if (key == 'RestaurantsGoodForGroups') {
                    key_words['group'] = 1;
                    key_words['groups'] = 1;
                } else if (key == 'RestaurantsTableService') {
                    key_words['table'] = 1;
                    key_words['service'] = 1;
                } else if (key == 'Caters') {
                    key_words['cater'] = 1;
                    key_words['caters'] = 1;
                }
            }

            str_key_words = JSON.stringify(key_words).replace(/\n/g, ' ').replace(/"/g, "'");
            // console.log(str_key_words);

            res.render('restaurants_recommendation.hbs', {
                pageTitle: 'Restaurants Recommendation',
                currentYear: new Date().getFullYear(),
                message: JSON.stringify(result.message, undefined, 2),
                restaurants: JSON.stringify(result.restaurants, undefined, 2),
                former_query: JSON.stringify(req.body, undefined, 2),
                key_words: str_key_words
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

// RESTful API
app.get('/reviews/business_id?', (req, res) => {
    model.getReviewByBusinessId(connection, req, res, function(result) {
        // console.log(result);
        recommendation_list = [];
        if ('business_id' in req.query) {
            // console.log(req.query.business_id);
            var temp_list = [];
            var curr_restaurant = pittsburgh_restaurants_dic[req.query.business_id];
            for (business_id in pittsburgh_restaurants_dic) {
                if (business_id == curr_restaurant.business_id) {
                    continue;
                }

                // Compute Similarity Score
                var score = 0;
                temp_restaurant = pittsburgh_restaurants_dic[business_id];
                if (curr_restaurant['Alcohol'] == temp_restaurant['Alcohol']) {
                    score += 1;
                }
                for (ambience in curr_restaurant['Ambience']) {
                    if (ambience in temp_restaurant['Ambience']) {
                        score += 1;
                    }
                }
                for (dietary in curr_restaurant['Dietary']) {
                    if (dietary in temp_restaurant['Dietary']) {
                        score += 1;
                    }
                }
                for (parking in curr_restaurant['Parking']) {
                    if (parking in temp_restaurant['Parking']) {
                        score += 1;
                    }
                }
                for (music in curr_restaurant['Music']) {
                    if (music in temp_restaurant['Music']) {
                        score += 1;
                    }
                }
                if (curr_restaurant['NoiseLevel'] == temp_restaurant['NoiseLevel']) {
                    score += 1;
                }
                if (curr_restaurant['PriceRange'] == temp_restaurant['PriceRange']) {
                    score += 1;
                }
                if (curr_restaurant['Attire'] == temp_restaurant['Attire']) {
                    score += 1;
                }
                for (good_for_meal in curr_restaurant['GoodForMeal']) {
                    if (good_for_meal in temp_restaurant['GoodForMeal']) {
                        score += 1;
                    }
                }
                for (best_night in curr_restaurant['BestNight']) {
                    if (best_night in temp_restaurant['BestNight']) {
                        score += 1;
                    }
                }
                for (other in curr_restaurant['Others']) {
                    if (other in temp_restaurant['Others']) {
                        score += 1;
                    }
                }

                temp_list.push(business_id + '\t' + score);
            }

            recommendation_list = temp_list.sort(function (a, b) {
                var id_a = a.split('\t')[0];
                var score_a = parseInt(a.split('\t')[1]);
                var id_b = b.split('\t')[0];
                var score_b = parseInt(b.split('\t')[1]);

                if (score_a != score_b) {
                    return score_a - score_b;
                } else {
                    return id_a - id_b;
                }
            }).slice(0, 10);

            model.getBusinessByBusinessId(connection, recommendation_list, res, function(rows) {
                // console.log(rows.business);
                model.getNumUsersReviewedBothRestaurants(connection, req.query.business_id, res, function(results) {
                    // console.log(results.businesses);
                    res.render('review_by_business_id.hbs',{
                        pageTitle: 'See Reviews by Businesses',
                        currentYear: new Date().getFullYear(),
                        message: JSON.stringify(result.message),
                        reviews: JSON.stringify(result.reviews),
                        name: req.query.name,
                        key_words: req.query.key_words,
                        similar_list: JSON.stringify(rows.businesses),
                        user_review_restaurants_recommendations: JSON.stringify(results.businesses)
                    });
                });
            });
        } else {
            res.render('review_by_business_id.hbs',{
                pageTitle: 'See Reviews by Businesses',
                currentYear: new Date().getFullYear(),
                message: JSON.stringify(result.message),
                reviews: JSON.stringify(result.reviews),
                name: req.query.name,
                key_words: req.query.key_words
            });
        }
    });
});

// RESTful API
app.get('/reviews/user_id?', (req, res) => {
    model.getReviewByUserId(connection, req, res, function(result) {
        // console.log(result);
        res.render('review_by_user_id.hbs',{
            pageTitle: 'See Reviews by User',
            currentYear: new Date().getFullYear(),
            message: JSON.stringify(result.message),
            reviews: JSON.stringify(result.reviews),
            user_id: req.query.user_id,
            key_words: req.query.key_words
        });
    });
});



app.listen(port);
console.log(`Starting server at localhost:${port}`);
