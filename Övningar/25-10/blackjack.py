from itertools import combinations

number_of_stacks = 2
game_cards = [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4], [5,5,5,5], [6,6,6,6], [7,7,7,7], [8,8,8,8], [9,9,9,9], [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], [11,11,11,11]]
number_of_game_cards = 0
for index, s in enumerate(game_cards):
    game_cards[index] = s * number_of_stacks
    number_of_game_cards += len(game_cards[index])

player_cards = [[],[],[],[],[],[],[],[],[],[]]
dealer_cards = [[],[],[],[],[],[],[],[],[],[]]
opponent_cards = [[],[],[],[],[],[],[],[],[],[]]

def partition(lst, n):
    count = 0
    for sample in list(combinations(lst, 4)):
        if sum(sample) == n:
            count += 1
    return count

print(partition([2, 1, 1, 1, 2, 1, 2, 2, 1], 6))

def calculation():
    sum = 0
    for index, _ in enumerate(player_cards):
        sum += len(player_cards[index])*(index+1)
    if sum >= 21:
        return 0
    #parts = partition(21-sum, 21-sum)
    #for card_set in parts:
    #    for card in card_set:
    #        print(len(game_cards[card_set-1])/number_of_game_cards)


game = True
while game:
    calculation()
    wrong_input = False
    card_drawn = input("Enter card:")
    number_of_game_cards -= 1
    match card_drawn:
        case "1":
            game_cards[0] = game_cards[0][1:]
        case "2":
            game_cards[1] = game_cards[1][1:]
        case "3":
            game_cards[2] = game_cards[2][1:]
        case "4":
            game_cards[3] = game_cards[3][1:]
        case "5":
            game_cards[4] = game_cards[4][1:]
        case "6":
            game_cards[5] = game_cards[5][1:]
        case "7":
            game_cards[6] = game_cards[6][1:]
        case "8":
            game_cards[7] = game_cards[7][1:]
        case "9":
            game_cards[8] = game_cards[8][1:]
        case "10":
            game_cards[8] = game_cards[9][1:]
        case "11":
            game_cards[0] = game_cards[0][1:]
            card_drawn = "1"
        case _:
            number_of_game_cards += 1
            print("Invalid card type")
            wrong_input = True

    if not wrong_input:
        entity = input("Who drew it:")
        match entity:
            case "player":
                player_cards[int(card_drawn)-1].append(int(card_drawn))
            case "dealer":
                dealer_cards[int(card_drawn)-1].append(int(card_drawn))
            case "opponent":
                opponent_cards[int(card_drawn)-1].append(int(card_drawn))
            case _:
                number_of_game_cards += 1
                print("Invalid entity type")
                game_cards[int(card_drawn)-1].append(int(card_drawn))