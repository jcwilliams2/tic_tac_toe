import random

empty_board = [["-", "-", "-"],
               ["-", "-", "-"],
               ["-", "-", "-"]]

placement_board = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

def randomMark():
    num = random.randint(1,2)
    if num == 1:
        return 'X'
    return 'O'

def printBoard(board):
    row_count = 0
    print('\n')
    for row in board:
        line = ""
        count = 0
        for block in row:
            block_segment = " " + str(block) + " "
            if count == 0 or count == 1:
                block_segment += "|"
            line += block_segment
            count += 1
        
            if count == 3:
                print(line)
        row_count += 1    
        if(row_count < 3):
            print("___________")

    print('\n')

class Player:
    def __init__(self, name):
        if name != "":
            self.name = name
        else:
            self.name = "Player1"
        self.mark = randomMark()

class Computer:
    def __init__(self, player):
        self.name = "CP"
        if player.mark == 'O':
            self.mark = 'X'
        else:
            self.mark = 'O'
        
#Game class keeps track of data from gameplay#       
class Game:
    def __init__(self, board):
        self.board = board

start = False

#Start of Gameplay#
print("Welcome to Tic-Tac-Toe!")
answer = input("Would you like to play? y/n ")
if(answer.lower() == 'y' or answer.lower() == 'yes'):
    name = input("Input player name: ")
    player = Player(name)
    cp = Computer(player)
    game = Game(placement_board)

    print(f'\nHello {player.name}!\nTo begin, you are "{player.mark}".')
    print('On your turn input the number in the area you would like to play.\nGood luck and here is your board!')

    printBoard(game.board)
    

else:
    print("Maybe another time. Goodbye.")

#printBoard(placement_board)

#player1 = Player('playerone')
#com = Computer(player1)





