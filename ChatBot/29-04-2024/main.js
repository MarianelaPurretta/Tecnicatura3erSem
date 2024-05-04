const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const genAI = new GoogleGenerativeAI("AIzaSyDr0QJwyKtxT3K7KmSVHiagr0dPrFoGG0c");

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('Un usuario se ha conectado');

  socket.on('chat message', async (msg) => {
    const prompt = msg + ". Actua siempre como una guia de turismo que se llama Adara y vive en argentina.";
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();

    io.emit('chat message', text);
  });

  socket.on('disconnect', () => {
    console.log('Usuario desconectado');
  });
});

server.listen(3000, () => {
  console.log('Escuchando en *:3000');
});
