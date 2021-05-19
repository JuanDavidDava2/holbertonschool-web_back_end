export default function groceriesList() {
  const groceryArray = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  const groceryMap = new Map();
  for (const item of groceryArray) groceryMap.set(item[0], item[1]);
  return groceryMap;
}
