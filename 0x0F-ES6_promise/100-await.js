import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((r) => ({ photo: r[0], user: r[1] }))
    .catch(() => ({ photo: null, user: null }));
}
