document.addEventListener('DOMContentLoaded', () => {  
  let coins = 0

  function coins2(number) {
    let cards = document.getElementsByClassName("card")
    for (let card = 0; card < cards.length; card++) {
        if (card.dataset.objectRef.inTavern === true) {
            console.log("w")
        }
  }}

  class Card {
    constructor(color, hp, dmg, inTavern = true, isGolden = false, cost = 3) {
        this.color = color;
        this.hp = hp;
        this.dmg = dmg;
        this.isGolden = isGolden;
        this.inTavern = inTavern;
        this.cost = cost;
    }
    
    summoncard(slotindex, side) {
        let cardslotlist = side === 2 ? document.getElementById("opponent-set").children :
                                        document.getElementById("player-set").children;
        let summonedCard = document.createElement('divCardList');
        summonedCard.classList.add("card");
        summonedCard.dataset.objectRef = this
        summonedCard.style.backgroundColor = this.color;
        cardslotlist[slotindex].appendChild(summonedCard);
    }

    RedOnBlue() {}
    RedOnYellow() {}
    RedOnGreen() {}
    RedOnBlack() {}
    RedOnWhite() {}
}

  //Makes it possible to drop cards
  document.addEventListener('dragover', e => {
      e.preventDefault();
      document.getElementById("coins-text").innerHTML = `Coins: ${coins}`
  });

  document.addEventListener('drop', e => {
      const draggedCard = document.querySelector('.card.dragging');
      if (draggedCard && e.target.classList.contains('card-slot') && e.target.children.length === 0 && e.target.classList.contains('shop-slot') === false) {
        draggedCard.parentNode.removeChild(draggedCard);
        e.target.appendChild(draggedCard);
      }
      else if (draggedCard && (e.target.id === "sell")) {
            draggedCard.parentNode.removeChild(draggedCard);
            coins += 1
            document.getElementById("coins-text").innerHTML = `Coins: ${coins}`
      }
      if (e.target.classList.contains("dropzone")) {
        e.target.classList.remove("dragover");
      }
  });

  document.addEventListener('dragstart', e => {
      if (e.target.classList.contains('card')) {
          e.target.classList.add('dragging');
          const offsetX = e.clientX - e.target.getBoundingClientRect().left;
          const offsetY = e.clientY - e.target.getBoundingClientRect().top;
          // Set the position of the card relative to the cursor
          e.dataTransfer.setDragImage(e.target, offsetX, offsetY);
      }
  });

  document.addEventListener('dragend', e => {
      if (e.target.classList.contains('card')) {
          e.target.classList.remove('dragging');
      }
  });
  document.addEventListener("dragenter", (e) => {
    if (e.target.classList.contains("dropzone")) {
      e.target.classList.add("dragover");
    }
  });
  
  document.addEventListener("dragleave", (e) => {
    if (e.target.classList.contains("dropzone")) {
      e.target.classList.remove("dragover");
    }
  });

const socket = io();

socket.emit('joinRoom')

socket.on("loadShop", (data) => {
  for (let i=0; i<=data.tier; i++) {
    var opponentSet = document.getElementById('opponent-set');
    var newCardSlot = document.createElement('div');
    newCardSlot.classList.add('card-slot');
    newCardSlot.classList.add('shop-slot');
    opponentSet.appendChild(newCardSlot);
  }
    let Yellow = new Card("yellow") 
    console.log("e")
    Yellow.summoncard(0, 2)
    Yellow.summoncard(1, 2)
    Yellow.summoncard(2, 2)
    Yellow.summoncard(3, 2)
    Yellow.summoncard(4, 2)
    Yellow.summoncard(5, 2)
});

let blue = new Card("blue");
blue.summoncard(0, 1);
let red = new Card("red");
red.summoncard(1, 1);
 
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
});