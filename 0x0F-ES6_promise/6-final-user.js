import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const lista = [];
      for (const value of results) {
        if (value.status === 'rejected') {
          value.value = value.reason.toString().substring(0, 40);
          delete value.reason;
        }
        lista.push(value);
      }
      return lista;
    });
}
