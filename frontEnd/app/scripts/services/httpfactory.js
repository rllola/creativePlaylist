'use strict';

/**
 * @ngdoc service
 * @name creativePlaylistApp.httpFactory
 * @description
 * # httpFactory
 * Factory in the creativePlaylistApp.
 */
angular.module('creativePlaylistApp')
  .factory('HttpFactory', function ($http) {

    var HttpFactory = {};
    var bitAuth = window.bitauth;
    var urlBase = 'http://0.0.0.0:8000/api/v1/'

    HttpFactory.connection = function(sin, service) {
      var url = urlBase + service + '/?format=json';
      var options = {
        url: url,
        headers: {
          'x-identity': bitAuth.getPublicKeyFromPrivateKey(sin),
          'x-signature': bitAuth.sign(url, sin)
          }
      };

      /*console.log(options.headers);
      console.log(bitAuth.getSinFromPublicKey(options.headers['x-identity']));*/

      $http.defaults.headers.common['x-identity'] = options.headers['x-identity'];
      $http.defaults.headers.common['x-signature'] = options.headers['x-signature'];

      return $http.get(options.url, options.headers);
    };

    return HttpFactory;
  });
