const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/YelpData', (err, db) => {
  if (err) {
    return console.log('Unable to connect to MongoDB server');
  }
  console.log('Connected to MongoDB server');

  db.collection('Todos').find({completed: true}).toArray().then((docs) => {
    console.log('Todos');
    console.log(JSON.stringify(docs, undefined, 2));
  }, (err) => {
    return console.log('Unable to fetch data', err);
  });

  db.close();
});
