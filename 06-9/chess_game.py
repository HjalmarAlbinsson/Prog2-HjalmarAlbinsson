game = True
board = []
board_width = 8
board_length = 8
<<<<<<< HEAD

=======
team_1 = "White"
team_2 = "Black"
team_3 = "Red"
team_4 = "Blue"
team_1_number_of_moves = 0
team_2_number_of_moves = 0
team_3_number_of_moves = 0
team_4_number_of_moves = 0
teams_dictionary = {team_1: team_1_number_of_moves, team_2: team_2_number_of_moves, team_3: team_3_number_of_moves, team_4: team_4_number_of_moves}

# ToDO
# make a function that calculates all "threatened" squares and store them in a list, each move.
# make a function that calculates all "possible" moves per piece and store them in a list.
# when trying to make a move, instead of calculating where it can go / take, just grab data from lists.
# add more pieces
# add utility i.e Spells, Tools, and more.
# make it online
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935

def generate_board():
    global board
    print("Generating board...")
    for w in range(0, board_width):
        coordinates_list = []
        for l in range(0, board_length):
            coordinates_list.append(0)
        board.append(coordinates_list)
    for p in pieces:
        board[p.x][p.y] = p


def get_square_data(x, y):
    exists = False
    is_habited = None
    piece_name = None
    team = None
    piece = None
    if len(board) > x:
        if len(board[x]) > y:
            exists = True
            if board[x][y] != 0:
                is_habited = True
                piece_name = board[x][y].name
                team = board[x][y].team
                piece = board[x][y]
            else:
                is_habited = False
    return [exists, is_habited, piece_name, team, piece]
<<<<<<< HEAD

def is_square_threatened(x, y, team):
    for piece in pieces:
        if piece.team != team:
            for coords in piece.threatened_squares:
                if coords == (x, y):
                    return True
    return False

def get_local_pos(direction, x, y, ):
    if direction == "north":
        return [x, y]
    elif direction == "east":
        return [(board_length - 1) - y, x]
    elif direction == "south":
        return [(board_width - 1) - x, (board_length - 1) - y]
    elif direction == "west":
        return [y, (board_width - 1) - x]


=======


def get_local_pos(direction, x, y, ):
    if direction == "north":
        return [x, y]
    elif direction == "east":
        return [(board_length - 1) - y, x]
    elif direction == "south":
        return [(board_width - 1) - x, (board_length - 1) - y]
    elif direction == "west":
        return [y, (board_width - 1) - x]


>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
def get_global_pos(direction, x, y, ):
    if direction == "north":
        return [x, y]
    elif direction == "east":
        return [y, (board_width - 1) - x]
    elif direction == "south":
        return [(board_width - 1) - x, (board_length - 1) - y]
    elif direction == "west":
        return [(board_length - 1) - y, x]

<<<<<<< HEAD
def update_boards_actionable_squares(x1, y1, x2, y2):
    for piece in pieces:
        for a_s in piece.seen_squares:
            if a_s == (x1, y1) or a_s == (x2, y2):
                piece.update_piece_actionable_squares(piece)
                break

class Team:
    def __init__(self, name):
        self.name = name
        self.number_of_moves = 0
=======
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935

class Piece:
    def __init__(self, x, y, direction, value, name, team):
        self.x = x
        self.y = y
<<<<<<< HEAD
        self.direction: str = direction
=======
        self.direction = direction
        self.value = value
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
        self.name = name
        self.team = team
        self.local_x = get_local_pos(self.direction, self.x, self.y)[0]
        self.local_y = get_local_pos(self.direction, self.x, self.y)[1]
<<<<<<< HEAD
        self.seen_squares = []
        self.threatened_squares = []


    def make_move(self, x, y, squares_to_take):
=======

    def make_move(self, x, y, squares_to_take):
        global team_1_number_of_moves, team_2_number_of_moves, team_3_number_of_moves, team_4_number_of_moves

>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
        print(self.team + "'s " + self.name + " moved to " + str(x) + ", " + str(y))
        if len(squares_to_take) > 0:
            for j in range(0, len(squares_to_take)):
                victim = get_square_data(squares_to_take[j][0], squares_to_take[j][1])[4]
                if victim is not None:
                    print("And killed " + victim.team + "'s " + victim.name)
                    board[squares_to_take[j][0]][squares_to_take[j][1]] = 0
                    del victim
        board[self.x][self.y] = 0
        board[x][y] = self
<<<<<<< HEAD
        update_boards_actionable_squares(x, y, self.x, self.y)
=======
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
        self.x = x
        self.y = y
        self.local_x = get_local_pos(self.direction, self.x, self.y)[0]
        self.local_y = get_local_pos(self.direction, self.x, self.y)[1]
<<<<<<< HEAD
        for team in teams:
            if self.team == team:
                team.number_of_moves += 1
        
        def update_seen_squares(seen_squares):
            self.seen_squares = seen_squares
        def update_threatened_squares(threatened_squares):
            self.threatened_squares = threatened_squares
=======
        if self.team == team_1:
            team_1_number_of_moves += 1
        if self.team == team_2:
            team_2_number_of_moves += 1
        if self.team == team_3:
            team_3_number_of_moves += 1
        if self.team == team_4:
            team_4_number_of_moves += 1

>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935

class Pawn(Piece):
    def move(self, requested_x, requested_y):
        if get_square_data(requested_x, requested_y)[0]:
            squares_to_take = []
            local_requested_x = get_local_pos(self.direction, requested_x, requested_y)[0]
            local_requested_y = get_local_pos(self.direction, requested_x, requested_y)[1]
            # Forward 2 steps
            if local_requested_y == self.local_y + 2 and local_requested_x == self.local_x and \
                    get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 1)[0],
                                    get_global_pos(self.direction, self.local_x, self.local_y + 1)[1])[1] is False and \
                    get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 2)[0],
                                    get_global_pos(self.direction, self.local_x, self.local_y + 2)[1])[1] is False and \
<<<<<<< HEAD
                    self.team.number_of_moves == 0:
=======
                    teams_dictionary[self.team] == 0:
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
                return super().make_move(requested_x, requested_y, squares_to_take)
            elif local_requested_y == self.local_y + 1:
                # Forward 1 steps
                if local_requested_x == self.local_x and \
                        get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 1)[0],
                                        get_global_pos(self.direction, self.local_x, self.local_y + 1)[1])[1] is False:
                    return super().make_move(requested_x, requested_y, squares_to_take)
                # Forward 1 step + Right 1 step
                elif local_requested_x == self.local_x + 1 and \
                        get_square_data(get_global_pos(self.direction, self.local_x + 1, self.local_y + 1)[0],
                                        get_global_pos(self.direction, self.local_x + 1, self.local_y + 1)[1])[
                            1] is True:
                    squares_to_take = [get_global_pos(self.direction, self.local_x + 1, self.local_y + 1)]
                    return super().make_move(requested_x, requested_y, squares_to_take)
                # Forward 1 step + Left 1 step
                elif local_requested_x == self.local_x - 1 and \
                        get_square_data(get_global_pos(self.direction, self.local_x - 1, self.local_y + 1)[0],
                                        get_global_pos(self.direction, self.local_x - 1, self.local_y + 1)[1])[
                            1] is True:
                    squares_to_take = [get_global_pos(self.direction, self.local_x - 1, self.local_y + 1)]
                    return super().make_move(requested_x, requested_y, squares_to_take)
            return print("You can't park there, Sir!")
<<<<<<< HEAD
    
    def update_piece_actionable_squares(self):
        seen_squares = []
        # Forward 2 steps
        if get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 1)[0],
                                get_global_pos(self.direction, self.local_x, self.local_y + 1)[1])[1] is False and \
                get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 2)[0],
                                get_global_pos(self.direction, self.local_x, self.local_y + 2)[1])[1] is False and \
                self.team.number_of_moves == 0:
            seen_squares.append(get_global_pos(self.direction, self.local_x, self.local_y + 1))

            # Forward 1 steps
            if get_square_data(get_global_pos(self.direction, self.local_x, self.local_y + 1)[0],
                                    get_global_pos(self.direction, self.local_x, self.local_y + 1)[1])[1] is False:
                seen_squares.append(get_global_pos(self.direction, self.local_x, self.local_y + 1))
            # Forward 1 step + Right 1 step
            if get_square_data(get_global_pos(self.direction, self.local_x + 1, self.local_y + 1)[0],
                                    get_global_pos(self.direction, self.local_x + 1, self.local_y + 1)[1])[1] is True:
                seen_squares.append(get_global_pos(self.direction, self.local_x + 1, self.local_y + 1))
            # Forward 1 step + Left 1 step
            if get_square_data(get_global_pos(self.direction, self.local_x - 1, self.local_y + 1)[0],
                                    get_global_pos(self.direction, self.local_x - 1, self.local_y + 1)[1])[1] is True:
                seen_squares.append(get_global_pos(self.direction, self.local_x - 1, self.local_y + 1))
=======
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935


class King(Piece):
    def move(self, requested_x, requested_y):
<<<<<<< HEAD
        if get_square_data(requested_x, requested_y)[0] and get_square_data(requested_x, requested_y)[1] is False:
=======
        if get_square_data(requested_x, requested_y)[0]:
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
            local_requested_x = get_local_pos(self.direction, requested_x, requested_y)[0]
            local_requested_y = get_local_pos(self.direction, requested_x, requested_y)[1]
            if local_requested_y == self.local_y + 1:
                # Forward 1 step +- Right/Left 1 step
                if local_requested_x == self.local_x or local_requested_x == self.local_x + 1 or local_requested_x == self.local_x - 1:
                    return super().make_move(requested_x, requested_y, [[requested_x, requested_y]])
            elif local_requested_y == self.local_y - 1:
                # Backward 1 step +- Right/Left 1 step
                if local_requested_x == self.local_x or local_requested_x == self.local_x + 1 or local_requested_x == self.local_x - 1:
                    return super().make_move(requested_x, requested_y, [[requested_x, requested_y]])
            elif local_requested_y == self.local_y:
                # Right/Left 1 step
                if local_requested_x == self.local_x or local_requested_x == self.local_x + 1 or local_requested_x == self.local_x - 1:
                    return super().make_move(requested_x, requested_y, [[requested_x, requested_y]])
            else:
                return print("You can't park there, Sir!")

<<<<<<< HEAD
teams = [Team("white"), Team("black")]
pieces = [Pawn(0, 1, "north", 1, "Pawn", teams[0]), Pawn(1, 1, "north", 1, "Pawn", teams[0]), Pawn(5, 6, "south", 1, "Pawn", teams[1]), Pawn(6, 6, "south", 1, "Pawn", teams[1])]
generate_board()

print(board)
=======
pieces = [King(0, 0, "north", 1, "King", "White"), Pawn(1, 7, "north", 1, "Pawn", "Black")]
generate_board()

pieces[0].move(0, 1)
pieces[0].move(0, 2)
pieces[0].move(0, 3)
pieces[0].move(0, 4)
pieces[0].move(0, 5)
pieces[0].move(1, 6)
pieces[0].move(1, 7)
print(board)

# def get_move():
#     move = input("Input move: ")
#     check_move(turn, move)
#
#
# def check_move():
#     print("Checking move")
#
#
# def update_board():
#     print("Updated board")
#
#
# while game == True:
#     get_move()
#     check_move()
#     update_board()
>>>>>>> 2c9b5a809dc0776e51baf718c1cee85b524db935
