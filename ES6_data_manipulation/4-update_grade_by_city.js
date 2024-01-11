export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsCity = students.filter((student) => student.location === city);
  const updatedStudents = studentsCity.map((student) => {
    const newgrades = newGrades.find((grade) => grade.studentId === student.id);
    if (newgrades) {
      return { ...student, grade: newgrades.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return updatedStudents;
}
