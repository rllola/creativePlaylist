'use strict';

/**
 * @ngdoc directive
 * @name creativePlaylistApp.directive:player
 * @description
 * # player
 */
angular.module('creativePlaylistApp')
  .directive('player', function () {
    return {
      template: '<audio controls>Your browser does not support the audio element.</audio>',
      song: '=song',
      restrict: 'E',
      scope : {
      	song: '=song'
      },
      link: function postLink(scope, element, attrs) {
        //element.text('this is the player directive');
        scope.$watch('song', function(value){
        	if(value){
            	console.log(value);
                console.log(element[0]);
            }
        });
      }
    };
  });
