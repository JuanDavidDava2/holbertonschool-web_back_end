export default function hasValuesFromArray(set, array) {
  return array.every((el) => set.has(el));
}
