// 5-payment.test.js

const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', function () {
    let consoleSpy;

    beforeEach(function () {
        // Create a spy on console.log before each test
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        // Restore console.log after each test
        consoleSpy.restore();
    });

    it('should log "The total is: 120" when called with 100 and 20', function () {
        sendPaymentRequestToApi(100, 20);

        // Verify the expected output and call count
        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
    });

    it('should log "The total is: 20" when called with 10 and 10', function () {
        sendPaymentRequestToApi(10, 10);

        // Verify the expected output and call count
        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
    });
});
