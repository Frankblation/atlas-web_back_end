const http = require('http');
const countStudents = require('./3-read_file_async');
const fs = require('fs');

// Create the server and assign it to the variable 'app'
const app = http.createServer((req, res) => {
  const { url } = req;

  if (url === '/') {
    // Home route
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    // Students route
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');
    
    // Get the database file from the command line argument
    const databaseFile = process.argv[2];

    // If no database file is provided, throw an error
    if (!databaseFile) {
      res.end('Cannot load the database\n');
    } else {
      // Call countStudents and handle promise
      countStudents(databaseFile)
        .then((output) => {
          res.end(output);
        })
        .catch((err) => {
          res.end(`${err.message}\n`);
        });
    }
  } else {
    // For any other route
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('404 Not Found\n');
  }
});

// Listen on port 1245
app.listen(1245);

// Export the 'app' variable
module.exports = app;
