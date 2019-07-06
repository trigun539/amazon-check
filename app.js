const Datastore = require('nedb');
const DB = new Datastore({filename: './amazon.db'});
const URL =
  'https://www.amazon.com/Seagate-BarraCuda-Internal-2-5-Inch-ST5000LM000/dp/B01M0AADIX/ref=sr_1_1?qid=1562377974&s=gateway&sr=8-1';
const {get} = require('axios');
const cheerio = require('cheerio');


db.loadDatabase(err => {
  if (err) {
    console.log('Unable to load database');
    process.exit();
  }
});

get(URL).then(res => {
  const $ = cheerio.load(res.data);

  const title = $('#productTitle')
    .text()
    .trim();
  let price = $('#priceblock_ourprice')
    .text()
    .trim();
  price = parseFloat(price.substr(1, price.length));

  console.log(title);
  console.log(price);
});
