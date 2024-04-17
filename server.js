const express = require('express');
const { createServer } = require('http');
const { promisify } = require('util');
const path = require('path');
const fs = require('fs');

const app = express();

// Serve the Flask app from the dist folder
app.use(express.static(path.join(__dirname, 'dist')));

// Create an HTTP server
const server = createServer(app);

// Promisify the server.listen function
const listen = promisify(server.listen);

// Start the server
async function startServer() {
  try {
    await listen(process.env.PORT || 5000);
    console.log('> Ready on http://localhost:5000');
  } catch (err) {
    console.error('Error starting the server:', err);
  }
}

startServer();