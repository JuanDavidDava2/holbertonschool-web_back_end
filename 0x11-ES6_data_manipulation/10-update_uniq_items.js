export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  for (const el of map) if (el[1] === 1) map.set(el[0], 100);
  return map;
}
