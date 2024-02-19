// server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const PORT = process.env.PORT || 3000;

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static(__dirname + '/public'));

io.on('connection', (socket) => {
    console.log('a user connected');

    // Add to database
    players[socket.id] = {x : 0, y : 0, color : "black"};
    players_searching.push(socket.id);
    join_room(socket.id)

    // Broadcast new player
    socket.emit("loadExistingPlayers", players)
    io.emit('newPlayer', socket.id);

    socket.on('disconnect', () => {
        console.log('user disconnected');
        delete players[socket.id]
        delete players_searching[socket.id]
        io.emit('playerDisconnected', socket.id);
    });

    
    socket.on('loadShop', (socket) => {
      io.emit('loadShop', {tier: 5});
    });

    // Receive player click
    socket.on('playerClick', (data) => {
        io.emit('playerTeleport', { id: socket.id, position: data });
        players[socket.id].x = data.x;
        players[socket.id].y = data.y;
    });
});

server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

let players = {};
let players_searching = [];
let cardtierlimits = {"6": 1, "5": 2, "4": 3, "3": 4, "2": 5, "1": 6};

function join_room(player) {
  players_searching.push(player);
  room = ""
  player.join(room)
}