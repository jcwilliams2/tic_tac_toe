empty_board = [["-", "-", "-"],
               ["-", "-", "-"],
               ["-", "-", "-"]]

placement_board = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

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
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

class Computer:
    def __init__(self, mark):

        self.name = "CP"
        self.mark = mark
        

printBoard(placement_board)






