'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('AboutCtrl', function ($http, $scope) {
  
    $http.get("/users").success(function(data, status, headers, config){
      console.log("Success !")
      $scope.data = data;
    });
    
  });
