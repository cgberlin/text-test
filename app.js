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
    args: [data.number, data.msg, data.carrier, data.amount, data.userGmail, data.userPassword]
  }
  PythonShell.run('textmason.py', options, function (err) {
    if (err) throw err;
    console.log('finished');
  });
});

/**
 * Start Server
 */
http.createServer(app).listen(app.get('port'), function () {
  console.log('SERVER ENGAGED ON ' + app.get('port'));
});
