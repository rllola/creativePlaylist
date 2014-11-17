'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('MainCtrl', [ '$http', '$scope', '$sce', 'ngDialog', 'HttpFactory', 'localStorageService' ,
    function ($http, $scope, $sce, ngDialog, HttpFactory, localStorageService) {

  	console.log('MainCtrl');

    var bitAuth = window.bitauth;

    // Initialisation
    $scope.songs = [];
    $scope.user = null;
    $scope.selectedSong = null;

    /*
     * Function that open a dialog box with the QrCode scanner in it
     */
  	$scope.openDialog = function () {
        ngDialog.open({ template: 'templates/qrscanner.html' });
    };

    /*
     * Login function : return the username and the id 
     */
    $scope.login = function(inputSin, username) {

      $scope.user = {};

      console.log(inputSin);

      $scope.user.sin = inputSin;
      var service = 'login/'+username;

      console.log($scope.user.sin);

      var response = HttpFactory.connection($scope.user.sin,service);

      console.log(response);

      response.success(function(data, status, headers) {
        $scope.user.username = data.username;
        $scope.user.id = data.id;
        localStorageService.add('user', $scope.user);
      }).error(function(data, status, headers) {
        console.log(status);
        $scope.user = null;
      });
    };

    $scope.loadSong = function() {

      var service = 'song';
      var response = HttpFactory.connection($scope.user.sin,service);

      response.success(function(data, status, headers) {
        //console.log(data.objects);
        $scope.songs = data.objects;
        //$scope.selectedSong = $sce.trustAsResourceUrl('http://0.0.0.0:8000' + $scope.songs[0].songFile);
      }).error(function(data, status, headers) {
        console.log(status);
      });
    };

    $scope.selectSong = function(song) {
      console.log(" selectedSong : " + song.songFile);
      $scope.selectedSong = null;
      $scope.selectedSong = $sce.trustAsResourceUrl('http://0.0.0.0:8000' + song.songFile);
      console.log($scope.selectedSong);
    };

    if (localStorageService.get('sin')) {
      $scope.user = localStorageService.get('user');
      $scope.login($scope.user.sin, $scope.user.username);
      //console.log($scope.sin);
    } else {
      $scope.user = null;
    };

  }]);
