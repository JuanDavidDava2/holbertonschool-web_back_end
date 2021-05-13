export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) === 'string') this._name = name;
    else throw new Error(TypeError('name must be a String'));

    if (typeof (length) === 'number') this._length = length;
    else throw new Error(TypeError('length must be a Number'));

    if (Array.isArray(students) && students.every((val) => typeof (val) === 'string')) this._students = students;
    else throw new Error(TypeError('students must be an Array of Strings'));
  }

  set name(value) {
    if (typeof (value) === 'string') this._name = value;
    else throw new Error(TypeError('name must be a String'));
  }

  get name() {
    return this._name;
  }

  set length(value) {
    if (typeof (value) === 'number') this._length = value;
    else throw new Error(TypeError('length must be a Number'));
  }

  get length() {
    return this._length;
  }

  set students(value) {
    if (Array.isArray(value) && value.every((v) => typeof (v) === 'string')) this._students = value;
    else throw new Error(TypeError('students must be an Array of Strings'));
  }

  get students() {
    return this._students;
  }
}
