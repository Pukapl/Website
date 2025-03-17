import os
import random # docs.python.org/3/library/random.html
import strings

clear = lambda: os.system('clear') # clear console -- LINUX ONLY

Table = [ #invisible to user/used for processing
          ["-", "-", "-", "-", "-", "-"],
          ["-", "C", "C", "C", "C", "-"],
          ["-", "-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-", "-"],
          ["-", "-", "-", "S", "S", "-"],
          ["-", "-", "-", "-", "-", "-"]
        ]
ViewTable = [
          ["0", "1", "2", "3", "4", "5"],
          ["1", "-", "-", "-", "-", "-"],
          ["2", "-", "-", "-", "-", "-"],
          ["3", "-", "-", "-", "-", "-"],
          ["4", "-", "-", "-", "-", "-"],
          ["5", "-", "-", "-", "-", "-"]
        ]

def printTable(Table): # Python array rendering is bad but it works
   for i in range(len(Table)):
      print(Table[i])

def checkTable(Table): # Check the processing table to see if blank
  for i in range(len(Table)):
    for o in range(len(Table[i])):
      if Table[i][o] != "-":
        return False
  return True

def randomTable(Table): # INOP
   for i in range(len(Table)):
      for o in range(len(Table[i])):
         Table[i][o] = random.choice(string.ascii_letters)

Continue = True

while True:
    while Continue == True:
        TargetColumn = int(input("Enter the column number (1-5): "))
        TargetRow = int(input("Enter the row number (1-5): "))
        clear()
        print(TargetColumn, TargetRow)
        if Table[TargetRow][TargetColumn] != "-":
            Table[TargetRow][TargetColumn] = "-"
            ViewTable[TargetRow][TargetColumn] = "X"
            print("Hit!")
        else:
            ViewTable[TargetRow][TargetColumn] = "O"
            print("Miss!")

        printTable(ViewTable)
        if checkTable(Table):
            Continue = False
            print("You Win!")
        else:
            pass # nop

    break # temp
    #input("Play again?")