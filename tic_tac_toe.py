import random

print("Wellcome to Connect Four")
print("-------------------")

possibleletters = ["A","B","C","D","E","F","G"]
gameboard = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
  print("\n     A   B   C   D   E   F   G   ")
  for x in range(rows):
    print("/n   +----+----+----+----+----+----+")
    print(x, " |")
    for y in range(cols):
      if(gameBoard[x][y] == "😡"):
        print("",gameBoard[x][y])
      elif("", gameBoard[x][y] == "💩"):
        print("",gameBoard[x][y],)
      else:
        print(" ", gameBoard[x][y])
  print("\n   +----+----+----+----+----+----+" ) 

  printGameBoard()

