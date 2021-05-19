export default function getListStudentIds(array) {
  return array.reduce((accumulator, item) => accumulator + item.id, 0);
}
