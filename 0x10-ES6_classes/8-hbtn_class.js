export default class HolbertonClass {
  constructor(size, location) {
    if (typeof (size) === 'number') this._size = size;
    if (typeof (location) === 'string') this._location = location;
  }

  // Convert obj to a primitive value
  // https://www.geeksforgeeks.org/javascript-symbol-toprimitive-function/#:~:text=The%20symbol.,Symbol()%5BSymbol.

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this._location;
    if (hint === 'number') return this._size;
    return this;
  }
}
