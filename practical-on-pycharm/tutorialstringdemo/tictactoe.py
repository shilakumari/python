board = [['' for _ in range(3)] for _ in range(3)]
def print_board(board):
    for row in board:
        print('1'.join(board))
        print('-'*10)
    print(print_board(board))
#Incomplete
