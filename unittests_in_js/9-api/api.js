const express = require('express');
const app = express();
const port = 7865;

// Root endpoint
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// New /cart/:id endpoint with regex to enforce numeric id
app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});