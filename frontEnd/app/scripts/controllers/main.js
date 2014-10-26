'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('MainCtrl', [ '$http', '$scope', 'ngDialog', 'HttpFactory', 'localStorageService' ,
    function ($http, $scope, ngDialog, HttpFactory, localStorageService) {

  	console.log('MainCtrl');

    var bitAuth = window.bitauth;

    // Initialisation
    $scope.songs = [];

    /*
     * Function that open a dialog box with the QrCode scanner in it
     */
  	$scope.openDialog = function () {
        ngDialog.open({ template: 'templates/qrscanner.html' });
    };

    $scope.login = function(inputSin) {

      console.log(inputSin);

      $scope.sin = inputSin;
      var service = 'song';

      console.log($scope.sin);

      var response = HttpFactory.connection($scope.sin,service);

      console.log(response);

      response.success(function(data, status, headers) {
        console.log(data);
        console.log(status);
        console.log(headers);
        localStorageService.add('sin', $scope.sin);
        $scope.songs = data.objects;
      }).error(function(data, status, headers) {
        console.log(data);
        console.log(status);
        console.log(headers);
      });
    };

    if (localStorageService.get('sin')) {
      $scope.sin = localStorageService.get('sin');
      $scope.login();
    } else {
      $scope.sin = false;
    };

  }]);
