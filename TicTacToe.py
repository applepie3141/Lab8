# Andy Zhang
# started May 4th, 2020
# AP Create Task

'''
A text-based tic-tac-toe game against the computer opponent. 
The opponent can choose moves randomly, to choose semi-randomly, or to win or tie every game.
'''

from numpy import random

currentGrid = [ #Shows the current grid
    '','','',
    '','','',
    '','','']

def printableGrid(grid): #Adds whitespaces to all empty spots in the grid, for readibility
    for x in range(0, len(grid)):
        if grid[x] == '':
            grid.pop(x)
            grid.insert(x,' ')
    return grid


def printGrid(): #prints the current grid in a nice, readable fashion. Only works for monospace fonts.
    for x in range(0, len(currentGrid),3):
        print(printableGrid(currentGrid)[x]+' | '+printableGrid(currentGrid)[x+1]+' | '+printableGrid(currentGrid)[x+2])
        if x != 6:
            print('---------')

def threeInRow(): #checks to see if someone has won the game
    for x in range(0,7,3): #checks for rows
        if currentGrid[x]==currentGrid[x+1] and currentGrid[x+1]==currentGrid[x+2] and (currentGrid[x]=='X' or currentGrid[x]=="O"):
            print('Three in a row! ' + currentGrid[x] + ' won the game.')
            return True
    for x in range(3):
        if currentGrid[x]==currentGrid[x+3] and currentGrid[x+3]==currentGrid[x+6] and (currentGrid[x]=='X' or currentGrid[x]=="O"):
            print('Three in a column! ' + currentGrid[x] + ' won the game.')
            return True
    if ((currentGrid[0]==currentGrid[4] and currentGrid[4]==currentGrid[8]) or (currentGrid[2]==currentGrid[4] and currentGrid[4]==currentGrid[6])) and (currentGrid[4]=='X' or currentGrid[4]=="O"):
        print('Three in a diagonal! ' + currentGrid[4] + ' won the game.')
        return True
    else:
        return False

def isFull(): #checks to see if the grid has any empty squares left
    for x in currentGrid:
        if x != "X" and x != "O":
            return False
    else:
        return True

# Game startup
print('Hello, welcome to Tic-Tac-Toe! Select your difficulty.')
difficulty = input("Valid inputs: EASY, MEDIUM, or HARD ")
print(difficulty + " selected. Would you like to choose X's or O's? X goes first.")
order = input('Valid inputs: X or O ')


def plot(): #function for player to choose square
    if isFull() or threeInRow():
        pass
    print('Where would you like to place your '+order+'?')
    xCoord = int(input('Input x-coordinate: '))
    yCoord = int(input('Input y-coordinate: '))
    if currentGrid[((2-yCoord)*3)+xCoord] != 'X' and currentGrid[((2-yCoord)*3)+xCoord] != 'O':
        currentGrid[((2-yCoord)*3)+xCoord] = order
    else:
        print('Oops! That spot is already occupied.')
        plot()

def emptySquares(): #helper function for opponent(), returns a list of indeces of empty squares
    squares = []
    for x in range(len(currentGrid)): #creates indeces of empty squares
        if currentGrid[x] != 'X' and currentGrid[x] != 'O':
            squares.append(x)
    return squares

def twoInRow(user): #determines if there are two in a row, returns indeces of the squares that would make 3 in a row to win
    squares = []
    for x in range(0,7,3): #checks for rows
        if currentGrid[x] == user and currentGrid[x+1] == '' and currentGrid[x] == currentGrid[x+2] and x+1 not in squares:
            squares.append(x+1)
        if currentGrid[x] == user and currentGrid[x+2] == '' and currentGrid[x] == currentGrid[x+1] and x+2 not in squares:
            squares.append(x+2)
        if currentGrid[x+1] == user and currentGrid[x] == '' and currentGrid[x+2] == currentGrid[x+1] and x not in squares:
            squares.append(x)
    for x in range(3):
        if currentGrid[x] == user and currentGrid[x+3] == '' and currentGrid[x] == currentGrid[x+6] and x+3 not in squares:
            squares.append(x+3)
        if currentGrid[x] == user and currentGrid[x+6] == '' and currentGrid[x] == currentGrid[x+3] and x+6 not in squares:
            squares.append(x+6)
        if currentGrid[x+3] == user and currentGrid[x] == '' and currentGrid[x+3] == currentGrid[x+6] and x not in squares:
            squares.append(x)
    if currentGrid[0] == user and currentGrid[4] == '' and currentGrid[0] == currentGrid[8] and 4 not in squares: #this part checks for the \ diagonal
        squares.append(4)
    if currentGrid[0] == user and currentGrid[8] == '' and currentGrid[0] == currentGrid[4] and 8 not in squares:
        squares.append(8)
    if currentGrid[4] == user and currentGrid[0] == '' and currentGrid[4] == currentGrid[8] and 0 not in squares:
        squares.append(0)
    if currentGrid[2] == user and currentGrid[4] == '' and currentGrid[2] == currentGrid[6] and 4 not in squares: #this part checks for the / diagonal
        squares.append(4)
    if currentGrid[2] == user and currentGrid[6] == '' and currentGrid[2] == currentGrid[4] and 6 not in squares:
        squares.append(6)
    if currentGrid[4] == user and currentGrid[2] == '' and currentGrid[4] == currentGrid[6] and 2 not in squares:
        squares.append(2)
    return squares
            

def opponent(diff):
    if isFull() or threeInRow():
        pass
    else:
        opp = ''
        if order == 'X':
            opp = 'O'
        elif order == 'O':
            opp = "X"
        print(emptySquares())
        if diff == 'EASY': #chooses randomly based on empty squares
            currentGrid[random.choice(emptySquares())] = opp
        if diff == 'MEDIUM': #prioritizes center square, then corners, then sides
            if 4 in emptySquares():
                currentGrid[4] = opp
            elif 0 in emptySquares():
                currentGrid[0] = opp
            elif 2 in emptySquares():
                currentGrid[2] = opp
            elif 6 in emptySquares():
                currentGrid[6] = opp
            elif 8 in emptySquares():
                currentGrid[8] = opp
            else:
                currentGrid[random.choice(emptySquares())] = opp
        if diff == 'HARD': #same as medium, but prioritizes spots that would win or would prevent a win
            if len(twoInRow(opp)) > 0:
                currentGrid[random.choice(twoInRow(opp))] = opp
            elif len(twoInRow(order)) > 0:
                currentGrid[random.choice(twoInRow(order))] = opp
            elif 4 in emptySquares():
                currentGrid[4] = opp
            elif 0 in emptySquares():
                currentGrid[0] = opp
            elif 2 in emptySquares():
                currentGrid[2] = opp
            elif 6 in emptySquares():
                currentGrid[6] = opp
            elif 8 in emptySquares():
                currentGrid[8] = opp
            else:
                currentGrid[random.choice(emptySquares())] = opp



currentGrid = [
    '','','',
    '','','',
    '','','']
printGrid()
print('Remember to input your points as if it were a coordinate place.\ni.e. 0,0 is in the bottom left and 2,2 is the top right.')
while not threeInRow() and not isFull():
    if order == 'X':
        plot()
        opponent(difficulty)
        printGrid()
    elif order == 'O':
        opponent(difficulty)
        printGrid()
        plot()

if isFull() and not threeInRow():
    print("Cat's game! The game ended in a tie.")
