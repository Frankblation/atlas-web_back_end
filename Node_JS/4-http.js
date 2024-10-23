const http = require('http');

// Create the server and assign it to the variable 'app'
const app = http.createServer((req, res) => {
  // Set response header to plain text
  res.setHeader('Content-Type', 'text/plain');
  
  // Send the response body "Hello Holberton School!"
  res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245);

// Export the 'app' variable
module.exports = app;
