'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:QrscannerctrlCtrl
 * @description
 * # QrscannerctrlCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('QrScannerCtrl', function ($scope) {

  	console.log('Qrscanner controller')

    /*
  	 *	Sucess of the QrCode reading
  	 */
    $scope.onSuccess = function(data) {
		  console.log(data);
	  };

  	/*
  	 *	Fail of the QrCode reading
  	 */
	$scope.onError = function(error) {
		console.log(error);
	};

  	/*
  	 *	Video error function
  	 */
	$scope.onVideoError = function(error) {
		console.log(error);
	};

  });
