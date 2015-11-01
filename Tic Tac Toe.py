# SALMANs TIC TAC TOE

# Global variables
playersTurn = "X"
allbuttons = []
p1 = 0
p2 = 0
draw = 0

from tkinter import *
import tkinter.messagebox
import os
import sys


# --------------------------------ALL FUNCTIONS-----------------------------------------

# Check which players turn it is
def turnChecker(button):
    # print("This is the button number: " + str( button ))

    if allbuttons[button]["text"] == " ":
        allbuttons[button]["text"] = playersTurn
        checkWinner()
        changeTurn()


# change turn after every move
def changeTurn():
    global playersTurn
    if playersTurn == "X":
        playersTurn = "O"
    else:
        playersTurn = "X"

    header.configure(text="Tic Tac Toe \n it is " + playersTurn + "s go!")


# Check for wins or draws
def checkWinner():

    global p1
    global p2
    global draw
    
    # check for horizontal wins
    for x in range(0, 9, 3):
        if (allbuttons[x]["text"] == playersTurn and allbuttons[x + 1]["text"] == playersTurn and allbuttons[x + 2][
            "text"] == playersTurn):
            if playersTurn == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(playersTurn)

    # check for vertical wins
    for x in range(0, 3, 1):
        if (allbuttons[x]["text"] == playersTurn and allbuttons[x + 3]["text"] == playersTurn and allbuttons[x + 6][
            "text"] == playersTurn):
            if playersTurn == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(playersTurn)

    # check for diagonal wins    
    if (allbuttons[0]["text"] == playersTurn and allbuttons[4]["text"] == playersTurn and allbuttons[8][
        "text"] == playersTurn or allbuttons[2]["text"] == playersTurn and allbuttons[4]["text"] == playersTurn and
            allbuttons[6]["text"] == playersTurn):
            if playersTurn == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(playersTurn)

    # check for draw    
    temp = 0
    for x in range (9):
        if (allbuttons[x]["text"] == "X" or allbuttons[x]["text"] == "O"):
            #print(draw)
            temp = temp+1

        #print('draw %d ' % draw )
        if temp == 9:
            draw = draw + 1


# Ask to play new game
def playAgain(winner):
    if winner == "X" or winner == "O":
        playAgainX = tkinter.messagebox.askyesno("WINNER", "The winner is %s \n Would you like to play again?" % winner)
        if playAgainX is True:
            reset()
        elif playAgainX is False:
            tk.destroy()
    elif winner == "Draw":
        playAgainX = tkinter.messagebox.askyesno("Draw", "The game was a Draw \n Would you like to play again?")
        if playAgainX is True:
            reset()
        elif playAgainX is False:
            tk.destroy()


# Reset board for new game
def reset():
    for x in range(0, 9):
        player1.configure(text="Player 1: %d" %p1)
        player2.configure(text="Player 2: %d" %p2)
        Draws.configure(text="Draws: %d" %draw)
        allbuttons[x]["text"] = " "

def newgame():
    tk.destroy()
    import test # replace 'test' with your file name


# -----------------------------END ALL FUNCTIONS----------------------------------




# ------------------------------CREATE BOARD--------------------------------------

# Create and configure the layout
tk = Tk()
tk.title("Tic Tac Toe")
tk.configure(background='white')

# Menu bar
menubar = Menu(tk)
tk.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Game..", command=newgame)
submenu.add_command(label="Exit", command=tk.destroy)

# ---TOP FRAME---
# top label
header = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!", fg="black", bg="white", font=("Helvetica", 12))
header.grid(row=0, column=2)


# ---MIDDLE FRAME---
# This function is used to check wich row each box needs to go in
def rowChecker():
    rowX = 1
    if x == 0 or x == 1 or x == 2:
        rowX = 1
    elif x == 3 or x == 4 or x == 5:
        rowX = 2
    elif x == 6 or x == 7 or x == 8:
        rowX = 3
    return rowX


# This creates the board and the buttons and runs the game
for x in range(0, 9):
    button = "button" + str(x)
    coloumnX = 1
    rowXI = 1
    if x == 0 or x == 3 or x == 6:
        columnX = 1
        rowXI = rowChecker()
    elif x == 1 or x == 4 or x == 7:
        columnX = 2
        rowXI = rowChecker()
    elif x == 2 or x == 5 or x == 8:
        columnX = 3
        rowXI = rowChecker()

    print(x, rowXI, columnX)

    button = Button(tk, text=" ", height=7, width=14, command=lambda j=x: turnChecker(j))
    button.grid(row=rowXI, column=columnX)
    allbuttons.append(button)

# ---BOTTOM FRAME---
scoreboard = Label(tk, text="Scoreboard", fg="black", bg="white", font=("Helvetica", 12))
scoreboard.grid(row=4, column=2)

player1 = Label(tk, text="Player1: %d" %p1, fg="black", bg="white", font=("Helvetica", 12))
player1.grid(row=5,column=1)

player2 = Label(tk, text="Player2: %d" %p2, fg="black", bg="white", font=("Helvetica", 12))
player2.grid(row=5,column=2)

Draws = Label(tk, text="Draws: %d" %draw, fg="black", bg="white", font=("Helvetica", 12))
Draws.grid(row=5,column=3)

# -------------------------------END OF CREATE BOARD------------------------------------


# keep program open until user closes
tk.mainloop()
