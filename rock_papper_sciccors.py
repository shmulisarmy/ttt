import random

#keeps track of wins
scores = {
    'player': 0,
    'computer': 0
}

match = 0
#stops the game when someone wins

def match_result(player, computer):
    if player == computer:
        return 'player'
    else:
        for i in range(len(things)):
            if computer == things[i] and player == things[i-1]:
                return 'player'
            elif player == things[i] and computer == things[i-1]:
                return 'computer'

while True:
    match += 1

    print(f"match {match}!!!\n")

    things = ['rock', 'scissors', 'paper']
    player = input("pick either rock, paper or scissors: ")
    while player not in things:
        print ("invalid choice, try again!")
        player = input("pick either 'rock', 'paper' or 'scissors': ")
    computer = random.choice(things)
    print(f"computer picked {computer}")
    winner = match_result(player, computer)
    print(f"{winner} wins match {match}")
    scores[winner] += 1
    if scores['player'] == 3:
        print(f"player reached 3 first player wins")
        break
    elif scores['computer'] == 3:
        print(f"computer reached 3 first computer wins")
        break