import random

#keeps track of wins
pl, co = 0, 0 

round = 0
#stops the game when someone wins
while True:
    round += 1

    print(f"round {round}!!!\n")

    things = ['rock', 'sciccors','papper']
    player = input("pick either 'rock', 'papper' or 'sciccors': ")
    while player not in things:
        print ("invalid choice, try again!")
        player = input("pick either 'rock', 'papper' or 'sciccors': ")
    computer = random.choice(things)
    print(f"computer picked {computer}")
    if player == computer:
        print("its a draw\n")
    else:
        for i in range(len(things)):
            if computer == things[i] and player == things[i-1]:
                print(f'player wins round {round}\n')
                pl += 1
            elif player == things[i] and computer == things[i-1]:
                print(f'computer wins round {round}\n')
                co += 1
    if pl == 3:
        print(f"player reached 3 first player wins")
        break
    elif co == 3:
        print(f"computer reached 3 first computer wins")
        break