const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/YelpData', (err, db) => {
  if (err) {
    return console.log('Unable to connect to MongoDB server');
  }
  console.log('Connected to MongoDB server');

  db.collection('Todos').insertOne({
    text: 'Something to do',
    Completed: false
  }, (err, result) => {
    if (err) {
      return console.log('Unable to insert todo', err);
    }
    console.log(JSON.stringify(result.ops[0]._id.getTimestamp()), undefined, 2);
  });

  db.close();
});
