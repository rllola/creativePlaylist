'use strict';

describe('Directive: qrScanner', function () {

  // load the directive's module
  beforeEach(module('creativePlaylistApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<qr-scanner></qr-scanner>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the qrScanner directive');
  }));
});
