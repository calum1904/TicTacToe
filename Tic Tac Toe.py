# Imports
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog as sd 
import os
import sys
import random
import socket

# Global variables
allbuttons = []
p1 = 0
p2 = 0
draw = 0
gameTypeAi = True
turnNumber = 0
playersTurn = "X"
oppositePlayer = "O"
receivedMoves = []

#Ai moves
moves1 = [0,2,6,8]
moves2 = [4]
moves3 = [1,3,5,7]
 

# --------------------------------ALL FUNCTIONS-----------------------------------------
def setAi():
    global gameTypeAi
    gameTypeAi = True
    newgame()

def setMultiplayer():
   global gameTypeAi, client, playersTurn, oppositePlayer
   gameTypeAi = False

   root = Tk()
   root.withdraw()
   root.resizable(0,0)
   #Ask the user for an ip address and a port, if blank set to 'localhost' and '12345'
   ip = str(sd.askstring("IP Address", "Enter the ip address you want to connect to"))
   port1 = sd.askstring("Port Number", "Enter the port number you want to connect to")
   if (ip == ""):
       ip = 'localhost'
   if (port1 == ""):
       port1 = 12345

   #Server Connections
   client = socket.socket()
   port = int(port1)
   client.connect((ip, port))
   #Receive a message from the server defining which player you are 'X' or 'O'
   assign = client.recv(1024)
   assign = assign.decode('utf-8').rstrip('\r\n')
   if assign == "X":
       playersTurn = "X"
       oppositePlayer = "O"
   elif assign == "O":
       playersTurn = "O"
       oppositePlayer = "X"

   print("You are player " + playersTurn)
   header.configure(text="Tic Tac Toe\nYou are player " + playersTurn)
   #'X' goes first to if you are 'O' the you have to wait by going straight to the recMove function
   if playersTurn == "O":
       recMove()
   
   


def recMove():
    global allbuttons, playersTurn, receivedMoves
    #Receive the move and decode it
    move = client.recv(1024)
    move = move.decode('utf-8').rstrip('\r\n')
    
    print("The other player click square: " + str(move))
    #Convert the move to a int and add it to a list of received moves
    move = int(move)
    receivedMoves.append(move)

    #Go through the list and change any squares that have been clicked by the opponent by checking the received moves
    for moves in receivedMoves:
        if playersTurn == "X":
            if allbuttons[moves]["text"] == " ":
                allbuttons[moves]["text"] = "O"
                checkWinner(oppositePlayer)
        elif playersTurn == "O":
            if allbuttons[moves]["text"] == " ":
                allbuttons[moves]["text"] = "X"
                checkWinner(oppositePlayer)
    


def ai():
    global playersTurn, moves1, moves2, moves3, allbuttons
    played = False
    if moves1 != []:
        for x in range(4):
            corners = random.choice(moves1)
            if allbuttons[corners]["text"] == " ":
                allbuttons[corners]["text"] = playersTurn
                moves1.remove(corners)
                print("Ai chose " + str(corners))
                print("remaining" + str(moves1))
                break
    elif moves2 != []:
            if allbuttons[4]["text"] == " ":
                allbuttons[4]["text"] = playersTurn
                moves2.remove(4)
                print("Ai chose " + "5")
                print("remaining" + str(moves2))
            
    elif moves3 != []:
        for x in range(4):
            everythingElse = random.choice(moves3)
            if allbuttons[everythingElse]["text"] == " ":
                allbuttons[everythingElse]["text"] = playersTurn
                moves3.remove(everythingElse)
                print("Ai chose " + str(everythingElse))
                print("remaining" + str(moves3))  
                break          
    changeTurn()
    checkWinner(playersTurn)


# Check which players turn it is
def turnChecker(button):
    # print("This is the button number: " + str( button ))
    global gameTypeAi, allbuttons, moves1, moves3, moves3, client, playersTurn
    if allbuttons[button]["text"] == " ":
        allbuttons[button]["text"] = playersTurn
        print ("You clicked square " + str(button))
        if button in moves1 and gameTypeAi == True:
            moves1.remove(button)
            print("Moves 1 remaining" + str(moves1))
        if button in moves2 and gameTypeAi == True:
            moves2.remove(button)
            print("Moves 2 remaining" + str(moves2))
        if button in moves3 and gameTypeAi == True:
            moves3.remove(button)
            print("Moves 3 remaining" + str(moves3))
        #If you're playing against someone then take the move, encode and send it to the server, then wait by going to the recMove function
        if gameTypeAi == False: 
            move = str(button)
            client.send( move.encode('utf-8'))
            checkWinner(playersTurn)
            recMove()
        else:
            changeTurn()


#change turn after every move
def changeTurn():
    global playersTurn
    
    if gameTypeAi == True:
        if playersTurn == "O":
            playersTurn = "X"
        else:
            playersTurn = "O"
            ai()
    if playersTurn == "X":
        playersTurn = "O"
        print(gameTypeAi)
    else:
        playersTurn = "O"
        if playersTurn == "X":
            playersTurn = "O"
            print(gameTypeAi)
        else:
            playersTurn = "X"

    header.configure(text="Tic Tac Toe \n it is " + playersTurn + "s go!")


# Check for wins or draws
def checkWinner(player):

    global p1, p2, draw, playersTurn

        
    # check for horizontal wins
    for x in range(0, 9, 3):
        if (allbuttons[x]["text"] == player and allbuttons[x + 1]["text"] == player and
            allbuttons[x + 2]["text"] == player):
            if player == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(player)

    # check for vertical wins
    for x in range(0, 3, 1):
        if (allbuttons[x]["text"] == player and allbuttons[x + 3]["text"] == player and
            allbuttons[x + 6]["text"] == player):
            if player == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(player)

    # check for diagonal wins    
    if (allbuttons[0]["text"] == player and allbuttons[4]["text"] == player and
        allbuttons[8]["text"] == player or allbuttons[2]["text"] == player and
        allbuttons[4]["text"] == player and allbuttons[6]["text"] == player):
            if player == "X":
                p1 = p1+1
            else:
                p2 = p2+1
                
            playAgain(player)

    # check for draw    
    temp = 0
    #if gameTypeAi == True:
     #   temp = temp + 1
    for x in range (0,9):
        if (allbuttons[x]["text"] == "X" or allbuttons[x]["text"] == "O"):
            temp = temp+1
        if temp == 9:
            draw = draw + 1
            playAgain("Draw")



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
    global playersTurn, gameTypeAi, moves1, moves2, moves3, receivedMoves
    receivedMoves = []
    for x in range(0, 9):
        player1.configure(text="Player 1: %d" %p1)
        player2.configure(text="Player 2: %d" %p2)
        Draws.configure(text="Draws: %d" %draw)
        allbuttons[x]["text"] = " "
    print (playersTurn)
    if gameTypeAi is True and playersTurn == "O":
        ai()
    moves1 = [0,2,6,8]
    moves2 = [4]
    moves3 = [1,3,5,7]

def newgame():
    global playersTurn, draw, p1, p2, moves1, moves2, moves3
    reset()
    playersTurn = "X"
    pl = 0
    p2 = 0
    draw = 0
    moves1 = [0,2,6,8]
    moves2 = [4]
    moves3 = [1,3,5,7]


def instruction():
    tkinter.messagebox.showinfo("Tic-Tac-Toe Instruction",
                                "X always goes first.\n\n"+
                                "Players alternate placing Xs and Os on the board until either (a) one player has three in a row\n\n"+
                                "horizontally, vertically or diagonally; or (b) all nine squares are filled.\n\n"+
                                "If a player is able to draw three Xs or three Os in a row, that player wins.\n\n"+
                                "If all nine squares are filled and neither player has three in a row, the game is a draw.")  

def About():
    tkinter.messagebox.showinfo("About",
                                "This game was developed by the following people.\n\n"+
                                "Calum Chamberlain\n\n"+
                                "Salman Fazal\n\n"+
                                "Prince Agyei Frimpong\n\n"+
                                "Sayed Askor Ali\n\n"+
                                "Muhammed Saqab\n\n"+
                                "Khadiza Yesmin\n\n"+
                                "This game was developed using Python version 3.4.3\n"+
                                "Copyright (c) 2015\n"+
                                "All Rights Reserved")

    tk.mainloop()

# -----------------------------END ALL FUNCTIONS----------------------------------
# ----------------------------------THEMES-------------------------------------------
def whiteTheme():
    tk.configure(background='white')
    
    # ---TOP FRAME---
    # top label
    header = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!", fg="black", bg="white", font=("Helvetica", 12))
    header.grid(row=0, column=2)

    # ---BOTTOM FRAME---
    scoreboard = Label(tk, text="Scoreboard", fg="black", bg="white", font=("Helvetica", 12))
    scoreboard.grid(row=4, column=2)

    player1 = Label(tk, text="Player1: %d" %p1, fg="black", bg="white", font=("Helvetica", 12))
    player1.grid(row=5,column=1)

    player2 = Label(tk, text="Player2: %d" %p2, fg="black", bg="white", font=("Helvetica", 12))
    player2.grid(row=5,column=2)

    Draws = Label(tk, text="Draws: %d" %draw, fg="black", bg="white", font=("Helvetica", 12))
    Draws.grid(row=5,column=3)
    
    
def blackTheme():
    tk.configure(background='black')
    
    # ---TOP FRAME---
    # top label
    header = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!", fg="white", bg="black", font=("Helvetica", 12))
    header.grid(row=0, column=2)
    # ---BOTTOM FRAME---
    scoreboard = Label(tk, text="Scoreboard", fg="white", bg="black", font=("Helvetica", 12))
    scoreboard.grid(row=4, column=2)

    player1 = Label(tk, text="Player1: %d" %p1, fg="white", bg="black", font=("Helvetica", 12))
    player1.grid(row=5,column=1)

    player2 = Label(tk, text="Player2: %d" %p2, fg="white", bg="black", font=("Helvetica", 12))
    player2.grid(row=5,column=2)

    Draws = Label(tk, text="Draws: %d" %draw, fg="white", bg="black", font=("Helvetica", 12))
    Draws.grid(row=5,column=3)

def blueTheme():
    tk.configure(background='blue')
    
    # ---TOP FRAME---
    # top label
    header = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!", fg="Red", bg="blue", font=("Helvetica", 12))
    header.grid(row=0, column=2)

    # ---BOTTOM FRAME---
    scoreboard = Label(tk, text="Scoreboard", fg="Red", bg="blue", font=("Helvetica", 12))
    scoreboard.grid(row=4, column=2)

    player1 = Label(tk, text="Player1: %d" %p1, fg="Red", bg="blue", font=("Helvetica", 12))
    player1.grid(row=5,column=1)

    player2 = Label(tk, text="Player2: %d" %p2, fg="Red", bg="blue", font=("Helvetica", 12))
    player2.grid(row=5,column=2)

    Draws = Label(tk, text="Draws: %d" %draw, fg="Red", bg="blue", font=("Helvetica", 12))
    Draws.grid(row=5,column=3)

# -------------------------------END OF THEMES------------------------------------
# ------------------------------CREATE BOARD--------------------------------------

# Create and configure the layout
tk = Tk()
tk.title("Tic Tac Toe")
tk.configure(background='white')

# Menu bar
menubar = Menu(tk)
tk.config(menu=menubar)

#----File Menu----
submenu = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Game..", command=newgame)
submenu.add_command(label="Exit", command=tk.destroy)

#----Game Type Menu----
submenu2 = Menu(menubar)
menubar.add_cascade(label="Game Type", menu=submenu2)
submenu2.add_command(label="Multiplayer", command=setMultiplayer)
submenu2.add_command(label="Play against Ai", command=setAi)

#----Theme Menu-------
submenu3 = Menu(menubar)
menubar.add_cascade(label="Themes", menu=submenu3)
submenu3.add_command(label="White", command=whiteTheme)
submenu3.add_command(label="Blue", command=blueTheme)
submenu3.add_command(label="Black", command=blackTheme)

#----Help Menu-------
submenu4 = Menu(menubar)
menubar.add_cascade(label="Help", menu=submenu4)
submenu4.add_command(label="Instruction", command=instruction)
submenu4.add_command(label="About", command=About)

# ---TOP FRAME---
# top label
header = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!", fg="black", bg="white", font=("Helvetica", 12))
header.grid(row=0, column=2)


# ---MIDDLE FRAME---
# This function is used to check wich row each box needs to go in
# Example the first if says if the button is 0, 1 or 2 they need to be in the top row(1)
def rowChecker():
    buttonRow = 1
    if square == 0 or square == 1 or square == 2:
        buttonRow = 1
    elif square == 3 or square == 4 or square == 5:
        buttonRow = 2
    elif square == 6 or square == 7 or square == 8:
        buttonRow = 3
    return buttonRow


# This creates the board and the buttons and runs the game
for square in range(0, 9):
    button = "button" + str(square)
    if square == 0 or square == 3 or square == 6:
        buttonColumn = 1
        buttonRowX = rowChecker()
    elif square == 1 or square == 4 or square == 7:
        buttonColumn = 2
        buttonRowX = rowChecker()
    elif square == 2 or square == 5 or square == 8:
        buttonColumn = 3
        buttonRowX = rowChecker()

    button = Button(tk, text=" ", height=7, width=14, command=lambda j=square: turnChecker(j))
    button.grid(row=buttonRowX, column=buttonColumn)
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
