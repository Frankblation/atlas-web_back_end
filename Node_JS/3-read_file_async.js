const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      // Split the file content into lines and remove empty lines
      const lines = data.trim().split('\n').filter(line => line !== '');

      // Remove the header line (first line)
      const header = lines.shift();

      // Create a map to group students by field
      const studentsByField = {};

      // Process each line
      lines.forEach((line) => {
        const [firstName, , , field] = line.split(',');

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      });

      // Log the total number of students
      const totalStudents = lines.length;
      console.log(`Number of students: ${totalStudents}`);

      // Log the number of students per field
      for (const field in studentsByField) {
        const students = studentsByField[field];
        console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
      }
    })
    .catch((error) => {
      // Handle errors (e.g., file not found)
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
