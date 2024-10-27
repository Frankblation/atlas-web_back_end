import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './path_to_your_function'; // Adjust the path as needed

// Initialize the queue with Kue
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function () {
  // Enter test mode
  before(() => {
    queue.testMode.enter();
  });

  // Exit test mode and clear the queue after tests
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create two new jobs to the queue', function () {
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is the first notification' },
      { phoneNumber: '0987654321', message: 'This is the second notification' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check if the jobs were added
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate each job details
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
