const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;

  beforeEach(() => {
    // Set up the spy before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the spy after each test to keep tests isolated
    sinon.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', function() {
    sendPaymentRequestToApi(100, 20);

    // Check that console.log was called with the expected output
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    // Verify that console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', function() {
    sendPaymentRequestToApi(10, 10);

    // Check that console.log was called with the expected output
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    // Verify that console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
