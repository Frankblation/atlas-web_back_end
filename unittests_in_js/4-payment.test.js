const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  afterEach(() => {
    // Restore the original methods after each test to prevent conflicts
    sinon.restore();
  });

  it('should call Utils.calculateNumber with type "SUM", a = 100, b = 20 and return 10', function() {
    // Stub Utils.calculateNumber to return 10 always
    const calculateStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    // Spy on console.log to check the output
    const consoleSpy = sinon.spy(console, 'log');
    
    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Verify stub is called with specific arguments
    expect(calculateStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    
    // Verify console.log was called with the correct message
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
