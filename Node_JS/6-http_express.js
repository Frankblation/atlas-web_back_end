// Import the Express module
const express = require('express');

// Create an Express application
const app = express();

// Define a route for the root endpoint
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Make the app listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

// Export the app for testing or further use
module.exports = app;
