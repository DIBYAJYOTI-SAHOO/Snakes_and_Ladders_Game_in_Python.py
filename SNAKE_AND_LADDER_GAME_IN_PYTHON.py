import random
import sys

max_value = 100

def start():
    welcome_message()
    player1_name, player2_name = player_names()
    player1_intial_position = 0
    player2_intial_position = 0

    while True:
        name_input1 = input("\n" + player1_name + " Your turn." + "\n click on the enter button to roll thr dice")
        print("\n rolling.....................")
        dice = dice_value()
        player1_intial_position = snake_ladder(player1_name, player1_intial_position, dice)

        winner(player1_intial_position, player1_name)

        name_input2 = input("\n" + player2_name + "Your turn." + "\n click on the enter button to roll thr dice")
        print("\n rolling.....................")
        dice = dice_value()
        player2_intial_position = snake_ladder(player2_name, player2_intial_position, dice)

        winner(player1_intial_position, player2_name)

def welcome_message():
    message = "Welcome to Ludo King"
    print(message)


def player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("enter a name for first player: ")

    player2_name = None
    while not player2_name:
        player2_name = input("enter a name for second player: ")

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

snakes_killzone = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

snakes_ladderZone = {
    3:  20,
    6:  14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

def dice_value():
    dice_value = random.randint(1,6)
    print(dice_value)
    return dice_value

def snake_bite(old_value, current_value, player_name):
    print("\n oh no!!!!!")
    print("\n"+ player_name +"got a snake bite and down from " + str(old_value)+ " to " + str(current_value))

def snake_ladder_jump(old_value, current_value, player_name):
    print("\n oh yes!!!!!")
    print("\n"+ player_name +" climbed the ladder from " + str(old_value)+ " to " + str(current_value))

def winner(position,player_name):
    if max_value == position:
        print("\n Winner is" +player_name+"" )
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. \n\n")
        sys.exit()

def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > max_value:
        print("You need " + str(max_value - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))

    if current_value in snakes_killzone:
        final_value = snakes_killzone.get(current_value)
        snake_bite(current_value, final_value, player_name)

    elif current_value in snakes_ladderZone:
        final_value = snakes_ladderZone.get(current_value)
        snake_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

if __name__=="__main__":
    start()