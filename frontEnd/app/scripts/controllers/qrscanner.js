'use strict';

/**
 * @ngdoc function
 * @name creativePlaylistApp.controller:QrscannerctrlCtrl
 * @description
 * # QrscannerctrlCtrl
 * Controller of the creativePlaylistApp
 */
angular.module('creativePlaylistApp')
  .controller('QrScannerCtrl', function ($scope, $rootScope) {

  	console.log('Qrscanner controller')

    /*
  	 *	Sucess of the QrCode reading
  	 */
    $scope.onSuccess = function(data) {
		  console.log(data);
      var login = {
                    user : 'lola',
                    key : data
                  };
      $rootScope.$emit('successScan', login);
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
