turn = 1
game = True

board_width = 8
board_length = 8
board = []

class Piece:
    def __init__(self, colour, pos_x, pos_y, direction, value, name):
        self.colour = colour
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        if self.direction == "north":
            self.dir_coef = 1
            self.local_pos_y = self.pos_y
            self.local_pos_x = self.pos_x
        elif self.direction == "east":
            self.dir_coef = 1
            self.local_pos_y = self.pos_x
            self.local_pos_x = self.pos_y
        elif self.direction == "south":
            self.dir_coef = -1
            self.local_pos_y = self.pos_y
            self.local_pos_x = self.pos_x
        elif self.direction == "west":
            self.dir_coef = -1
            self.local_pos_y = self.pos_x
            self.local_pos_x = self.pos_y

    def move(self, x, y):
        print("Moved to " + str(x) + ", " + str(y))

class Pawn(Piece):
    def move(self, x, y):
        if [x, y] in board:
            if self.direction == "north" or self.direction == "west":
                new_local_pos_y = x
                new_local_pos_x = y

            if new_local_pos_y == self.local_pos_y + 2*self.dir_coef and new_local_pos_x == self.local_pos_x:
                return super().move(x, y)
            elif new_local_pos_y == self.local_pos_y + 1*self.dir_coef:
                if new_local_pos_x == self.local_pos_x + 1 or new_local_pos_x == self.local_pos_x - 1:
                    return super().move(x, y)
                
pawn1 = Pawn("white", 0, 0, "north", 1, "")
# knight2 = Pawn("black")

pawn1.move(1, 7)

def generate_board():
    print("Generating board")

def get_move():
    global turn
    turn = 3 - turn
    move = input("Input move: ")
    check_move(turn, move)

def check_move():
    print("Checking move")


def update_board():
    print("Updated board")


while game == True:
    get_move()
    check_move()
    update_board()
