'use strict';

describe('Service: bitAuth', function () {

  // load the service's module
  beforeEach(module('creativePlaylistApp'));

  // instantiate service
  var bitAuth;
  beforeEach(inject(function (_bitAuth_) {
    bitAuth = _bitAuth_;
  }));

  it('should do something', function () {
    expect(!!bitAuth).toBe(true);
  });

});
