export default function (firstName, lastName) {
    return Promise.resolve({
      firstName,
      lastName,
    });
  }