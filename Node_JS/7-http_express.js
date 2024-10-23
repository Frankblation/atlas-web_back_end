const express = require('express');
const fs = require('fs');
const path = require('path');
const countStudents = require('./3-read_file_async');  // Reuse function

const app = express();
const PORT = 1245;

// Route for "/"
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Route for "/students"
app.get('/students', (req, res) => {
    const databaseFile = process.argv[2];  // Get database file from command-line argument

    if (!databaseFile) {
        res.status(500).send('Database file is not provided');
        return;
    }

    // Reading the student data asynchronously
    countStudents(databaseFile)
        .then((output) => {
            res.send(`This is the list of our students\n${output}`);
        })
        .catch((err) => {
            res.status(500).send(`Error: Cannot load the database\n${err.message}`);
        });
});

// Listen on the specified port
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
