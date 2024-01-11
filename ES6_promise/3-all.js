import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      const { body: photoBody } = photoResponse;
      const { firstName, lastName } = userResponse.body;

      console.log(`${photoBody} ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.error('Signup system offline');
      return new Error();
    });
}
