const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with correct arguments and return 10', function() {
    // Stub Utils.calculateNumber to return 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    // Spy on console.log
    const spy = sinon.spy(console, 'log');

    // Call the function with arguments
    sendPaymentRequestToApi(100, 20);

    // Assert that Utils.calculateNumber was called with correct arguments
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    // Assert that console.log was called with the correct message
    expect(spy.calledWith('The total is: 10')).to.be.true;

    // Restore the stub and spy
    stub.restore();
    spy.restore();
  });
});
