'use strict';

describe('Controller: QrscannerctrlCtrl', function () {

  // load the controller's module
  beforeEach(module('creativePlaylistApp'));

  var QrscannerctrlCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    QrscannerctrlCtrl = $controller('QrscannerctrlCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
