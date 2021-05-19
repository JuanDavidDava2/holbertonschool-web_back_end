export default function getStudentsByLocation(array, city, grad) {
  return array
    .filter((item) => item.location === city)
    .map((student) => {
      const gradeItem = grad
        .filter((item) => item.studentId === student.id)
        .map((x) => x.grade)[0];
      const grade = gradeItem || 'N/A';
      return { ...student, grade };
    });
}
