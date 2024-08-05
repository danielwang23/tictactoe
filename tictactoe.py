
import random


#Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True
gameMode = None         # Option for player to choose GameMode

player1_wins = 0
player2_wins = 0
computer_wins = 0
starting_player = "X"   # Track who starts the game

# Printing the game board
def printBoard(board):
    # ANSI escape codes directly for color coding in the terminal
    for i in range(0, 9, 3):
        row = ""
        for j in range(3):
            cell = board[i + j]
            if cell == "X":
                row += "\033[91m" + cell + "\033[0m"  # Red for X
            elif cell == "O":
                row += "\033[94m" + cell + "\033[0m"  # Blue for O
            else:
                row += cell
            if j < 2:
                row += " | "
        print(row)
        if i < 6:
            print("---------")
    
    # ===== Original Code if choose not to use ANSI escape codes above to form table =======
    # print(board[0] + " | " + board[1] + " | " + board[2])
    # print("---------")
    # print(board[3] + " | " + board[4] + " | " + board[5])
    # print("---------")
    # print(board[6] + " | " + board[7] + " | " + board[8])


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
    global gameRunning, player1_wins, player2_wins, computer_wins
    if checkDiagonal(board) or checkHorizontal(board) or checkVert(board):
        printBoard(board)   # Shows the Final Board
        print(f"The Winner is {winner}")
        gameRunning = False
        if winner == "X":
            if gameMode == "PP":
                player1_wins += 1      
            else:
                player1_wins += 1      # If gamemode is PvP then add win to Player X no matter what if Player X wins
        elif winner == "O":
            if gameMode == "PP":
                player2_wins += 1
            else:
                computer_wins += 1
        displayWinTotals()              # Displays Totals vs each player
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
            # switchPlayer()
            print(f"Computer has made a move at position {position}")
            break


# Restart the game
def restartGame():
    global board, currentPlayer, winner, gameRunning, starting_player
    restart = input("Do you want to play again? (y/n): ").lower()
    if restart == 'y':
        board = ["-", "-", "-", 
                 "-", "-", "-", 
                 "-", "-", "-"]
        currentPlayer = "X"
        winner = None
        gameRunning = True
        # Alternate starting player
        starting_player = "O" if starting_player == "X" else "X"
        currentPlayer = starting_player
        main()        # Restart the main loop
    else:
        gameRunning = False
        print("Thanks for playing!")


# Display win totals
def displayWinTotals():
    if gameMode == "PP":
        print(f"Player 1 (X) Total Wins: {player1_wins}")
        print(f"Player 2 (O) Total Wins: {player2_wins}")
    else:
        print(f"Player Wins: {player1_wins}")
        print(f"Computer Wins: {computer_wins}")


# Main game loop
def main():
    global gameRunning, gameMode
    gameMode = input("Would you like to play Player vs. Player (Type PP) or Player vs. Computer (Type C)? ").upper()
    while gameMode not in ["PP", "C"]:
        gameMode = input("Invalid choice. Please type PP for Player vs Player or C for Player vs Computer: ").upper()
    
    if gameMode == "PP":
        print("You have selected Player vs Player mode.")
    elif gameMode == "C":
        print("You have selected Player vs Computer mode.")


    while gameRunning:
        printBoard(board)
        if winner != None:
            break
        if gameMode == "PP" or (gameMode == "C" and currentPlayer == "X"):    # If it's Player vs Player or Player's turn in PvC, take player input
            playerInput(board)
        elif gameMode == "C" and currentPlayer == "O":                        # If it's Player vs Computer and Computer's turn, make computer move
            computer(board)
        checkGameWin()
        checkTie(board)
        switchPlayer()



main()  # Starts the main loop initially


#-------------WHAT I WANT TO IMPLEMENT FURTHER------------

#Want to create a tab that keeps track of score between two players Player 1 and 2 and can reset the score.
#Create a system that randomly alternates between who goes first Player 1 vs Player 2
#Always have player 1 go first in PvP and PvC



#=========Extremely Advanced============
# Create a TKINTER frame and add all this code to it.
#Allow one central area to pick modes for PvP or PvC, or grid size(3x3 vs 5x5 vs 7x7)
#Train the computer to get better with AI libraries
#Expand the grid to be not just 3x3 but 4x4 or 5x5
#Change UI and UX Design, colors of terminal.