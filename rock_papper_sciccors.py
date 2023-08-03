import random

#keeps track of wins
scores = {
    'player': 0,
    'computer': 0
}

match = 0

things = ['rock', 'scissors', 'paper']
#stops the game when someone wins

def get_player_input():
    player = input("pick either rock, paper or scissors: ")
    while player not in things:
        print ("invalid choice, try again!")
        player = get_player_input()
    return player


def run_match(player):
    computer = get_compuer_choice()
    winner = match_result(player, computer)
    print(f"{winner} wins match {match}")
    scores[winner] += 1

def get_compuer_choice():
    computer = random.choice(things)
    print(f"computer picked {computer}")
    return computer
def match_result(player, computer):
    if player == computer:
        print("Draw! Starting match over:")
        return match_result(get_player_input(), get_compuer_choice())
    else:
        for i in range(len(things)):
            if computer == things[i] and player == things[i-1]:
                return 'player'
            elif player == things[i] and computer == things[i-1]:
                return 'computer'

while True:
    match += 1

    print(f"match {match}!!!\n")

    player = get_player_input()
    run_match(player)
    if scores['player'] == 3:
        print(f"player reached 3 first player wins")
        break
    elif scores['computer'] == 3:
        print(f"computer reached 3 first computer wins")
        break