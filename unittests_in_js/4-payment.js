const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with correct arguments and return 10', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spy = sinon.spy(console, 'log');

    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Check if Utils.calculateNumber was called with the right arguments
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;
    
    // Check if console.log was called once with the expected message
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('The total is: 10')).to.be.true;

    // Restore the stub and spy after the test
    stub.restore();
    spy.restore();
  });
});
