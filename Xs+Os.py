import random
import sys


boxes = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]] 


def intToText(num):
    if (num == 0): return ' '
    if (num == 1): return 'O'
    if (num == 2): return 'X'


def printGrid():
    print('┌─┬─┬─┐' '\n'
          '│' + intToText(boxes[0][0]) + '│' + intToText(boxes[1][0]) + '│' + intToText(boxes[2][0]) + '│' '\n'
          '├─┼─┼─┤' '\n'
          '│' + intToText(boxes[0][1]) + '│' + intToText(boxes[1][1]) + '│' + intToText(boxes[2][1]) + '│' '\n'
          '├─┼─┼─┤' '\n'
          '│' + intToText(boxes[0][2]) + '│' + intToText(boxes[1][2]) + '│' + intToText(boxes[2][2]) + '│' '\n'
          '└─┴─┴─┘')

def checkVictory():

    for i in range(0, 3):
        for j in range(0, 3):

            if (boxes[i][j] == 0):
                continue

            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]: 

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = boxes[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0]
                        boxToCheck[1] += vector[1]

                        if (boxes[boxToCheck[0]][boxToCheck[1]] != charToCheckFor):
                            break

                        if (x == 2):
                            return intToText(boxes[i][j])

                except:
                    continue
    return ' '

def chooseComputerMove():

    #This just fills a list with all the empty boxes and chooses one at random
    emptyBoxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if (boxes[i][j] == 0):
                emptyBoxes += [[i, j]]

    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]





print('\n' 'Welcome to X\'s and O\'s, Lets play!')
printGrid()

while(1):


    while(1): #Loop until valid input is entered

        move = input('\n' 'Your turn. Make a move:' '\n')

        if (len(move) == 3):
            if (1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3): #Check the user has entered valid coordinates
                if (boxes[int(move[0]) - 1][int(move[2]) - 1] == 0): #Check that the chosen box is empty
                    boxes[int(move[0]) - 1][int(move[2]) - 1] = 2 #Put an X in the box
                    printGrid()
                    break

        print('Invalid input.')

        # Checks if player has won
    victoryResult = checkVictory()
    if (victoryResult == 'X'):
        print ('Well done you win!')
        break



    # Computers move
    computerMove = chooseComputerMove()
    boxes[computerMove[0]][computerMove[1]] = 1
    print('\n' 'My turn!')
    printGrid()

    

    # Check of the computer has won
    victoryResult = checkVictory()
    if (victoryResult == 'O'):
        print ('Sorry I win!')
        break


