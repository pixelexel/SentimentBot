var twit = require('twit');
var pythonShell = require('python-shell');
var config = require('./config.js');

var pyshell = new pythonShell('tweet.py');
var Twitter = new twit(config);


var post_sentiment = function(message) {
    var params = {
        q: '@sentimentsbot',  // REQUIRED
        result_type: 'recent',
        lang: 'en'
    }

    Twitter.get('search/tweets', params, function(err, data) {
      // if there no errors
        if (!err) {
          // grab ID of tweet to post_sentiment
            var tweetText = data.statuses[0].text;

            if(tweetText) { //if tweets exist

              var textArray = tweetText.split(' ');

              //Send keyword
              pyshell.send(textArray[1]);

              //Receive sentiment
              pyshell.on('message', function(message){

                Twitter.post('statuses/update', {status : message}, function(err, response) {

                    if (response) {
                        console.log('Success!');
                    }
                    if (err) {
                        console.log('Something went wrong while posting... Duplication maybe...');
                    }
                });

              });

              pyshell.end(function (err) {
                if (err) console.log(err);
              });

            }

        }
        // if unable to Search a tweet
        else {
          console.log('Something went wrong while SEARCHING...',err);
        }
    });
}

post_sentiment();

setInterval(post_sentiment, 60000);
