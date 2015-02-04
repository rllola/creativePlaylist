'use strict';

/**
 * @ngdoc directive
 * @name creativePlaylistApp.directive:player
 * @description
 * # player
 */
angular.module('creativePlaylistApp')
  .directive('player', function ($sce, $rootScope) {
    return {
      template: '<audio id="audio" autoplay controls ></audio>',
      restrict: 'EA',
      scope : {
      	song: '=song',
      	songs: '=songs'
      },
      link: function(scope, element, attrs) {
      	//var audio = new Audio();
      	var audio = document.getElementById('audio');

        scope.$watch('song', function(value){
        	console.log(value);
        	if(value){
            	audio.src = $sce.trustAsResourceUrl('http://192.168.1.111:8000' + value.songFile);
		    	$(".main").css({
		        	'background-image': 'url(http://192.168.1.111:8000' + value.art.artImage +')'
		      	});
		      	audio.load();
		      	audio.play();
            }
            console.log(scope.song);
        });

        /* Ugly need to change it */
    	audio.addEventListener('ended', function(){ 
    		$rootScope.$broadcast('nextSong');
      	});
      }
    };
  });
