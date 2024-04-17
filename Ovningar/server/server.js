// server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const PORT = process.env.PORT || 3000;
const app = express();
const server = http.createServer(app);
const io = socketIo(server);
app.use(express.static(__dirname + '/public'));

const gameData = {};
let roomID = 0;

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

io.on('connection', (socket) => {
  console.log('A user connected');
  socket.on('requestJoinRoom', () => {joinRoom(socket)});  
  socket.on('requestLeaveRoom', () => {leaveRoom(socket)});
  socket.on('requestLoadEnemy', (socket) => {loadEnemy(socket)});
  socket.on('requestLoadShop', (socket) => {loadShop(socket)});
});

joinRoom(socket) {
  if (io.sockets.adapter.rooms.get(roomID).size === 0)
    {roomID ++;};
}

loadShop(socket) {
  io.emit('loadShop');
}