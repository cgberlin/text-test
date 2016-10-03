/*global require*/

/**
 * Dependencies
 */
var express = require('express'),
  http = require('http'),
  bodyParser = require('body-parser'),
  compress = require('compression'),
  path = require('path'),
  app = express(),
  resources = path.join(__dirname, 'pages');
var PythonShell = require('python-shell');
var passport = require('passport');
var FacebookStrategy = require('passport-facebook').Strategy;


passport.use(new FacebookStrategy({
    clientID: '1801954643381344',
    clientSecret: "a73787f6640bf5263062ddaeba009eb0",
    callbackURL: "http://localhost:3000/auth/facebook/callback"
  },
  function(accessToken, refreshToken, profile, cb) {
    User.findOrCreate({ facebookId: profile.id }, function (err, user) {
      return cb(err, user);
    });
  }
));


/**
 * Configuration
 */
//Port to be listen, by default 3000
app.set('port', process.env.PORT || 3000);
//Compress stream
app.use(compress());
//Set static resources from the path in pages
app.use(express.static(resources));
//Parse information
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));
//Set headers on the communication client server.
app.use(function (req, res, next) {
  //Expose server to everyone who wants to consume it
  res.setHeader('Access-Control-Allow-Origin', "*");
  res.header("Access-Control-Allow-Headers", "Content-Type, X-API-KEY");
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  return next();
});
app.get('/mason', function(req, res) {
  var data = req.query;
  var options = {
    args: [data.number, data.msg, data.carrier, data.amount, data.userGmail, data.userPassword, data.mainPassword]
  }
  PythonShell.run('textmason.py', options, function (err) {
    if (err) throw err;
    console.log('finished');
  });
});

app.get('/login/facebook',
  passport.authenticate('facebook'));

// handle the callback after facebook has authenticated the user
app.get('/login/facebook/callback',
    passport.authenticate('facebook', {
        successRedirect : '/main.html',
        failureRedirect : '/pages'
    }));


/**
 * Start Server
 */
http.createServer(app).listen(app.get('port'), function () {
  console.log('SERVER ENGAGED ON ' + app.get('port'));
});
