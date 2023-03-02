import random

print("Wellcome to Connect Four")
print("-------------------")

possibleletters = ["A","B","C","D","E","F","G"]
gameboard = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
  print("\n     A   B   C   D   E   F   G   ", end="")
  for x in range(rows):
    print("/n   +----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(gameBoard[x][y] == "😡"):
        print("",gameBoard[x][y], ends=" |")
      elif("", gameBoard[x][y] == "💩"):
        print("",gameBoard[x][y], ends=" |")
      else:
        print(" ", gameBoard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+" ) 

  printGameBoard()
