'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('MainCtrl', [ '$http', '$scope', '$sce', '$rootScope', 'ngDialog', 'HttpFactory', 'localStorageService' ,
    function ($http, $scope, $sce, $rootScope, ngDialog, HttpFactory, localStorageService) {

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
     * lola : 8babdc5ed9aebf3ba19b5fada61f2949fd2c72173982c68fbcb94c04da76b188
     */
    $scope.login = function(inputSin, username) {


      $scope.user = {};

      //console.log(inputSin);

      $scope.user.sin = inputSin;
      var service = 'login/'+username;

      //console.log($scope.user.sin);

      var response = HttpFactory.connection($scope.user.sin,service);

      //console.log(response);

      response.success(function(data, status, headers) {
        $scope.user.username = data.username;
        $scope.user.id = data.id;
        localStorageService.add('user', $scope.user);
      }).error(function(data, status, headers) {
        //console.log(status);
        $scope.user = null;
      });
    };

    $rootScope.$on('successScan', function(event, data) {
      //console.log(data);
      ngDialog.close();
      $scope.login(data.key, data.user);
    });

    $scope.loadSong = function() {

      var service = 'song';
      var response = HttpFactory.connection($scope.user.sin,service);

      response.success(function(data, status, headers) {
        //console.log(data.objects);
        $scope.songs = data.objects;
        //$scope.selectedSong = $sce.trustAsResourceUrl('http://0.0.0.0:8000' + $scope.songs[0].songFile);
      }).error(function(data, status, headers) {
        //console.log(status);
      });
    };

    $scope.selectSong = function(song) {
      console.log('selectSong');
      console.log($scope.selectedSong);
      $scope.selectedSong = song;
    };

    $scope.$on('nextSong', function() {
      for (var i = 0; i < $scope.songs.length; i++) {
        if ($scope.selectedSong.id === $scope.songs[i].id) {
          if ($scope.songs[i+1]) {
                  //console.log(scope.songs[i+1]);
                  $scope.selectedSong = $scope.songs[i+1];
                  $scope.$apply();
                  break;
          } else {
                  //console.log(scope.songs[0])
                  $scope.selectedSong = $scope.songs[0];
                  $scope.$apply();
                  break;
          }
        }
      }
    });
    
    if (localStorageService.get('user')) {
      $scope.user = localStorageService.get('user');
      $scope.login($scope.user.sin, $scope.user.username);
    } else {
      $scope.user = null;
    };

  }]);
