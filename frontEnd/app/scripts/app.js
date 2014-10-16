'use strict';

/**
 * @ngdoc overview
 * @name creativePlaylistApp
 * @description
 * # creativePlaylistApp
 *
 * Main module of the application.
 */
angular
  .module('creativePlaylistApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'snap'
  ])
  .config(function ($routeProvider, snapRemoteProvider) {

    /*Option pour snap.js */
    snapRemoteProvider.globalOptions = {
        maxPosition : 300,
        minPosition : -300
    };

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
