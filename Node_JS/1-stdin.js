// Display the initial message
console.log("Welcome to Holberton School, what is your name?");

// Listen for user input from stdin
process.stdin.on('data', (input) => {
    const name = input.toString().trim(); 
    // Display the user's name
    console.log(`Your name is: ${name}`);

    // If input comes from a pipe (like echo), we close stdin
    if (!process.stdin.isTTY) {
        process.stdin.end(); // Signal the end of input in case of pipe
    }
});

// When stdin ends (either piped or manual input), display closing message
process.stdin.on('end', () => {
    console.log("This important software is now closing");
});