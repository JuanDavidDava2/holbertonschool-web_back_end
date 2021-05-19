export default function cleanSet(set, startString) {
  let resultString = '';
  if (!startString || !startString.length) return resultString;
  set.forEach((el) => {
    if (el && el.startsWith(startString)) resultString += `${el.slice(startString.length)}-`;
  });
  return resultString.slice(0, resultString.length - 1);
}
