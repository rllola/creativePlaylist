'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
