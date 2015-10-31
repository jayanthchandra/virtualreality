var request = require('request');
var qs = require('querystring');

var url = 'https://yboss.yahooapis.com/ysearch/web';

var params = qs.stringify({
  q: 'Yahoo Mobile Developer Suite',
  format: 'json',
  count: '10',
});

var oauth = {
  consumer_key: 'dj0yJmk9T3N3b015TWF4SFEzJmQ9WVdrOU1uVnNhMWwwTXpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD04Yg--',
  consumer_secret: '4856a636a01997cc42b1c8dfa07a75a5c755e48b'
};

request.get({ url: url + '?' + params, oauth: oauth, json: true }, function(e, r, body) {
  console.log(body);
});
