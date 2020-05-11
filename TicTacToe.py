# Andy Zhang
# started May 4th, 2020
# AP Create Task

'''
A text-based tic-tac-toe game against the computer opponent. 
The opponent can choose moves randomly, to choose semi-randomly, or to win or tie every game.
'''

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
            print('row')
            return True, currentGrid[x]
    for x in range(3):
        if currentGrid[x]==currentGrid[x+3] and currentGrid[x+3]==currentGrid[x+6] and (currentGrid[x]=='X' or currentGrid[x]=="O"):
            print('column')
            return True, currentGrid[x]
    if ((currentGrid[0]==currentGrid[4] and currentGrid[4]==currentGrid[8]) or (currentGrid[2]==currentGrid[4] and currentGrid[4]==currentGrid[6])) and (currentGrid[4]=='X' or currentGrid[4]=="O"):
        print('diag')
        return True, currentGrid[4]
    else:
        print('false')
        return False

# Game startup
print('Hello, welcome to Tic-Tac-Toe! Select your difficulty.')
difficulty = input("Valid inputs: EASY, MEDIUM, or HARD ")
print(difficulty + " selected. Would you like to choose X's or O's? X goes first.")
order = input('Valid inputs: X or O ')

def plot():
    print('Where would you like to place your '+order+'?')
    xCoord = int(input('Input x-coordinate: '))
    yCoord = int(input('Input y-coordinate: '))
    if currentGrid[((2-yCoord)*3)+xCoord] == '':
        currentGrid[((2-yCoord)*3)+xCoord] = order
    else:
        print('Oops! That spot is already occupied.')
        plot()

currentGrid = [
    '','','',
    '','','',
    '','','']
printGrid()
print('Remember to input your points as if it were a coordinate place.\ni.e. 0,0 is in the bottom left and 2,2 is the top right.')
#threeInRow()
while threeInRow() == False:# and '' in currentGrid:
    plot()
    printGrid()


if threeInRow() == True:
    print('Three in a row! '+threeInRow()[1] + ' has won the game.')
else:
    print("Cat's game! The round has ended in a draw.")