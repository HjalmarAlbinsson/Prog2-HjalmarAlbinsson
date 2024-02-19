document.addEventListener('DOMContentLoaded', () => {

  class CardAbilitiesHandler {
    static handleDeathrattleGolem () {
        console.log("Summon a number of 1/1 Rat tokens equal to the number of friendly Beasts.");
        // Implement Golem's Battlecry logic here
    }

    // Define methods for other Battlecry abilities
  }
  
  class Card {
    constructor(color, inTavern = true, isGolden = false, clash = 1) {
        this.color = color;
        this.isGolden = false;
        this.inTavern = inTavern;
        this.clash = clash;
    }
    
    summoncard(slotindex) {
      const cardslotlist = document.getElementsByClassName("card-slot")
      let specificCard = document.createElement('divCardList');
      specificCard.classList.add("card");
      specificCard.style.backgroundColor = this.color;
      specificCard.draggable = true;
      cardslotlist[slotindex].appendChild(specificCard);
    }

    RedOnBlue() {}
}

// Example usage:
let blue = new Card("blue");
blue.summoncard(0);
let red = new Card("red");
red.summoncard(1);

  //Makes it possible to drop cards
  document.addEventListener('dragover', e => {
      e.preventDefault();
  });

  document.addEventListener('drop', e => {
      const draggedCard = document.querySelector('.card.dragging');
      if (draggedCard && e.target.classList.contains('card-slot') && e.target.children.length === 0) {
          e.target.appendChild(draggedCard);
      }
  });

  document.addEventListener('dragstart', e => {
      if (e.target.classList.contains('card')) {
          e.target.classList.add('dragging');
      }
  });

  document.addEventListener('dragend', e => {
      if (e.target.classList.contains('card')) {
          e.target.classList.remove('dragging');
      }
  });

const socket = io();

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let players = {};

socket.on('loadExistingPlayers', (data) => {
  players = Object.assign(players, data);
});

socket.on('newPlayer', (id) => {
  players[id] = { x: 0, y: 0, color: 'black' };
}); 

socket.on('playerDisconnected', (id) => {
    delete players[id];
});

socket.on('playerTeleport', (data) => {
    players[data.id].x= data.position.x;
    players[data.id].y = data.position.y;
});

socket.on("loadShop", (data) => {
  for (let i=0; i<=data.tier; i++) {
    var opponentSide = document.getElementById('opponent-side');
    var newCardSlot = document.createElement('div');
    newCardSlot.classList.add('card-slot');
    opponentSide.appendChild(newCardSlot);
}});
 
class InputHandler {
  static handleKeyPress(key) {
      switch (key) {
          case 's':
            socket.emit('loadShop', "e");
              break;
          case 'g':
              break;
          case 'ArrowLeft':
              break;
          case 'ArrowRight':
              break;
          case 'Space':
              break;
          default:
              break;
    }
  }
  static handleMouseClick(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    socket.emit('playerClick', { x, y });  
  }
}

document.addEventListener('keydown', (event) => {
    InputHandler.handleKeyPress(event.key);
});
canvas.addEventListener('click', (event) => {
    InputHandler.handleMouseClick(event);
});



function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    Object.entries(players).forEach(([id, player]) => {
        ctx.fillStyle = id === socket.id ? player.color : player.color;
        ctx.beginPath();
        ctx.arc(player.x, player.y, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
    });

    requestAnimationFrame(draw);
}

draw();
});