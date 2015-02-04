'use strict';

/**
 * @ngdoc directive
 * @name creativePlaylistApp.directive:qrScanner
 * @description
 * # qrScanner
 */
angular.module('creativePlaylistApp')
  .directive('qrScanner', ['$timeout', function($timeout) {
  return {
    restrict: 'E',
    scope: {
      ngSuccess: '&ngSuccess',
      ngError: '&ngError',
      ngVideoError: '&ngVideoError'
    },
    link: function(scope, element, attrs) {
    
      window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
    
      var height = attrs.height || 400;
      var width = attrs.width || 350;
      var localMediaStream;
    
      var video = document.createElement('video');
      video.setAttribute('width', width);
      video.setAttribute('height', height);
      var canvas = document.createElement('canvas');
      canvas.setAttribute('id', 'qr-canvas');
      canvas.setAttribute('width', width);
      canvas.setAttribute('height', height);
      canvas.setAttribute('style', 'display:none;'); 
    
      angular.element(element).append(video);
      angular.element(element).append(canvas);
      var context = canvas.getContext('2d'); 
    
      var scan = function() {
        if (localMediaStream) {
          context.drawImage(video, 0, 0, 307,250);
          try {
            qrcode.decode();
          } catch(e) {
            scope.ngError({error: e});
          }
        }
        $timeout(scan, 200);
      }

      var successCallback = function(stream) {
        console.log('successCallback');  
        video.src = (window.URL && window.URL.createObjectURL(stream)) || stream;
        localMediaStream = stream;

        video.play();
        //$timeout(scan, 1000);
        scan();
      }

      // Call the getUserMedia method with our callback functions
      if (navigator.getUserMedia) {
        navigator.getUserMedia({video: true}, successCallback, function(e) {
          scope.ngVideoError({error: e});
        });
      } else {
        scope.ngVideoError({error: 'Native web camera streaming (getUserMedia) not supported in this browser.'});
      }

      qrcode.callback = function(data) {
        localMediaStream.stop();
        localMediaStream = null;
        console.log('Houston, on a marché sur la lune.');
        scope.ngSuccess({data: data});
      };
    }
  }
}]);