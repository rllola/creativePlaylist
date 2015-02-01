//temporary bitauth server for sbex
//not using that middleware crap, just simple request from django.  this shouldn't be done over internet (at least without https)
//rewriting the below functions is a PITA so this will do for now


var express = require('express');
var bitauth = require('bitauth');


var app = express();

//dont need this insecure shit
//app.use(rawBody);
//app.use(bodyParser());


app.get('/getsin', function(req, res) {
        // Get the SIN from the public key
      console.log('getsin end point');
      var sin = bitauth.getSinFromPublicKey(req.query.pubkey);
      if(!sin){
          res.send(400, {error: 'Bad public key from identity'});
          //res.status(400).send({error: 'Bad public key from identity'})
       }else{
          res.send(200, sin)
          //res.status(200).send(sin)
       }

});


app.get('/verifysignature', function(req, res) {
    console.log(req.query.data)
    console.log('verifysignature end point');
    console.log(req.query.pubkey, req.query.signature);
    bitauth.verifySignature(req.query.data, req.query.pubkey, req.query.signature, function(err, result) {
      if(err || !result) {
        console.log("Ca passe pas");
        return res.send(400, {error: 'Invalid signature'});
      }else{
      //all good
        console.log("Ca passe");
        return res.send(200, "True")
      }
    });
});


app.listen(3000);
