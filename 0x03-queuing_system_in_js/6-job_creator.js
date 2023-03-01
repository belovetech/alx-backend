import { createQueue } from 'kue';

const queue = createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', {
  phoneNumber: '08109221864',
  message: 'Senior software enginner',
});

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', (err) => {
    console.log('NNotification job completed');
  })
  .on('failed', (err) => {
    console.log('Notification job failed');
  });

job.save();
