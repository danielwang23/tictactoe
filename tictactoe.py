
import random

#Global Variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Taking a player input
def playerInput(board):
    inp = int(input(f"Player {currentPlayer} Enter a number 1-9: "))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        if not(inp >=1 and inp <=9):
            print("Oops! Pick a number in range 1-9")
        else:
            print("Oops! Spot already taken, pick a different square.")


# Check for a win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
    return False
    

def checkVert(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
    return False
    

def checkDiagonal(board):
     global winner
     if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
     return False
     

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("The game is a tie!")
        gameRunning = False
        restartGame()


def checkGameWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVert(board):
        printBoard(board) #Shows the Final Board
        print(f"The Winner is {winner}")
        gameRunning = False
        restartGame()
        

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Computer move
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# Restart the game
def restartGame():
    global board, currentPlayer, winner, gameRunning
    restart = input("Do you want to play again? (y/n): ").lower()
    if restart == 'y':
        board = ["-", "-", "-", 
                 "-", "-", "-", 
                 "-", "-", "-"]
        currentPlayer = "X"
        winner = None
        gameRunning = True
        main()  # Restart the main loop
    else:
        gameRunning = False
        print("Thanks for playing!")


# Main game loop
def main():
    global gameRunning
    while gameRunning:
        printBoard(board)
        if winner != None:
            break
        playerInput(board)
        checkGameWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkGameWin
        checkTie(board)

main()  # Start the main loop initially



#Want to create a tab that keeps track of score between two players Player 1 and 2 and can reset the score.