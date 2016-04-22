def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################


    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
 

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
            (board['low-L'] == player and board['mid-L'] == player and board['top-L'] == player) or
            (board['low-M'] == player and board['mid-M'] == player and board['top-M'] == player) or
            (board['low-R'] == player and board['mid-R'] == player and board['top-R'] == player) or
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer                          # Chooses starting player.
    for i in range(9):                             # Creates loop of 9
        printBoard(board)                          # Displays board from above
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        board[move] = turn
        if( checkWinner(board, 'X') ):             #Checks if this turn won 
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):          #Checks if this turn won 
            print('O wins!')
            break
     
        if turn == 'X':                            # These 4 lines swaps player turns 
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
