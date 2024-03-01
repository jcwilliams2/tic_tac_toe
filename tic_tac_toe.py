import random

empty_board = [["-", "-", "-"],
               ["-", "-", "-"],
               ["-", "-", "-"]]

#initial gameboard#
placement_board = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

#generate player's mark for gameplay#
def randomMark():
    num = random.randint(1,2)
    if num == 1:
        return 'X'
    return 'O'

def printBoard(board):
    row_count = 0
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
    print("\n")


class Player:
    def __init__(self, name):
        if name != "":
            self.name = name
        else:
            self.name = "Player1"
        self.mark = randomMark()
        self.wins = 0
    
    def __repr__(self):
        return self.name
    
    def turn_position(self, game):
        position = 0
        while position not in game.playable:
            pos = input("Your turn: ")
            if pos != "":
                position = int(pos)
        return position

class Computer:
    def __init__(self, player):
        self.name = "CP"
        if player.mark == 'O':
            self.mark = 'X'
        else:
            self.mark = 'O'
        self.wins = 0

    def __repr__(self):
        return self.name

    def turn_position(self, game):
        possible = 0
        while possible not in game.playable:
            possible = random.randint(game.playable[0], game.playable[-1])
        return possible
        

        
#Game class keeps track of data from gameplay#       
class Game:
    def __init__(self, board, player, computer):
        self.play = True
        self.board = board
        self.player = player
        self.computer = computer
        self.playable = [1,2,3,4,5,6,7,8,9]
        self.game_end = False
        self.turnCount = 0
        self.gameCount = 1

    def win(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        else:
            return False
        
    def check_win(self, mark):
        win = self.win()
        if win:
            self.game_end = True
            if mark == self.player.mark:
                print(f'{self.player} has won the game.')
                self.player.wins += 1
            else:
                print(f'{self.computer} has won the game.')
                self.computer.wins += 1
        elif self.turnCount == 9:
            self.game_end = True
            print("Draw. Game Over.")

    def turn (self, place, mark):
        place_int = int(place)
        if place_int in self.playable:
            if place_int == 1:
                self.board[0][0] = mark
                self.playable.remove(1)
            elif place_int == 2:
                self.board[0][1] = mark
                self.playable.remove(2)
            elif place_int == 3:
                self.board[0][2] = mark
                self.playable.remove(3)
            elif place_int == 4:
                self.board[1][0] = mark
                self.playable.remove(4)
            elif place_int == 5:
                self.board[1][1] = mark
                self.playable.remove(5)
            elif place_int == 6:
                self.board[1][2] = mark
                self.playable.remove(6)
            elif place_int == 7:
                self.board[2][0] = mark
                self.playable.remove(7)
            elif place_int == 8:
                self.board[2][1] = mark
                self.playable.remove(8)
            else:
                self.board[2][2] = mark
                self.playable.remove(9)

            printBoard(self.board)
            self.turnCount += 1
            if(self.turnCount > 4):
                self.check_win(mark)
            return True
        else:
            print("Invalid move. Try Again.")
            return False
        
    def reset(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        self.playable = [1,2,3,4,5,6,7,8,9]
        self.game_end = False
        self.turnCount = 0
        self.gameCount += 1

start = False

#Start of Gameplay#
print("Welcome to Tic-Tac-Toe!")
answer = input("Would you like to play? y/n ")
if(answer.lower() == 'y' or answer.lower() == 'yes'):
    name = input("Input player name: ")
    player = Player(name)
    cp = Computer(player)
    game = Game(placement_board, player, cp)

    print(f'\nHello {player.name}!\nTo begin, you are "{player.mark}".')
    print('On your turn input the number in the area you would like to play.\nGood luck and here is your board!')
    while(game.play):
        print("\n")
        printBoard(game.board)
        position = player.turn_position(game)
        game.turn(position, player.mark)
        cp_turn = cp.turn_position(game)
        game.turn(cp_turn, cp.mark)

        position = player.turn_position(game)
        game.turn(position, player.mark)
        cp_turn = cp.turn_position(game)
        game.turn(cp_turn, cp.mark)

        position = player.turn_position(game)
        game.turn(position, player.mark)

        if game.game_end == False:
            cp_turn = cp.turn_position(game)
            game.turn(cp_turn, cp.mark)

        if game.game_end == False:
            position = player.turn_position(game)
            game.turn(position, player.mark)
    
        if game.game_end == False:
            cp_turn = cp.turn_position(game)
            game.turn(cp_turn, cp.mark)

        if game.game_end == False:
            position = player.turn_position(game)
            game.turn(position, player.mark)

        play_again = input("Would you like to play again? y/n ")
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            game.reset()
            print(f'Game {game.gameCount} is ready to begin!')
        else:
            game.play = False
            print("Thanks for playing!")    

else:
    print("Maybe another time. Goodbye.")
