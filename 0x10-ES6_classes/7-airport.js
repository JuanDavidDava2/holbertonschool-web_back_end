export default class Airport {
  constructor(name, code) {
    if (typeof name === 'string') this._name = name;
    if (typeof code === 'string') this._code = code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
