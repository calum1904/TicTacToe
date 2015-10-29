#Calum's TicTacToe code using Tkinter to make a GUI

from tkinter import *
import tkinter.messagebox

playersTurn = "X"

tk = Tk()
tk.title("Tic Tac Toe")

lable = Label(tk, text="Tic Tac Toe \n it is " + playersTurn + "s go!")
lable.grid(row = 0, column = 2, sticky = S+N+E+W)
allbuttons = []



#This checks if a player wins or not and changes playersTurn
def checkWinner():
    
    print(playersTurn)
    global playersTurn
    if playersTurn == "X":
        turnP = playersTurn
        playersTurn = "O"
    else:
        turnP = playersTurn
        playersTurn = "X"
    print(turnP)
        
    lable.configure(text = "Tic Tac Toe \n it is " + playersTurn + "s go!")

    # check for horizontal wins
    for x in range (0,9,3):
        if (allbuttons[x]["text"] == turnP and allbuttons[x+1]["text"] == turnP and allbuttons[x+2]["text"] == turnP):
            playAgain(turnP)

    # check for vertical wins
    for x in range (0,3,1):
        if (allbuttons[x]["text"] == turnP and allbuttons[x+3]["text"] == turnP and allbuttons[x+6]["text"] == turnP):
            playAgain(turnP)

    # check for diagonal wins    
    if (allbuttons[0]["text"] == turnP and allbuttons[4]["text"] == turnP and allbuttons[8]["text"] == turnP or allbuttons[2]["text"] == turnP and allbuttons[4]["text"] == turnP and allbuttons[6]["text"] == turnP):
            playAgain(turnP)
            
    # check for draw
    elif(1==1):
        draw = 0
        for x in range (9):
            if (allbuttons[x]["text"] == "X" or allbuttons[x]["text"] == "O"):
                print(draw)
                draw = draw+1


            print('draw %d ' % draw )
            if draw == 9:
                playAgain("Draw")
          
def reset():
    for x in range(0,9):
        allbuttons[x]["text"] = " "

def playAgain(winner):
    if winner == "X" or winner == "O":
            playAgainX = tkinter.messagebox.askyesno("WINNER", "The winner is %s \n Would you like to play again?" %winner)
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
            
#This function checks whos turn it is and wether or not they can click that box
def turnChecker(button):
    print("This is the button number: " + str( button ))
    
    if allbuttons[button]["text"] == " " and playersTurn == "X":
        allbuttons[button]["text"] = "X"
        checkWinner()
    
    elif allbuttons[button]["text"] == " " and playersTurn == "O":
        allbuttons[button]["text"] = "O"
        checkWinner()
        

#This function is used to check wich row each box needs to go in
def rowChecker():
    rowX = 1
    if x == 0 or x == 1 or x == 2:
        rowX = 1
    elif x == 3 or x == 4 or x == 5:
        rowX = 2
    elif x == 6 or x == 7 or x == 8:
        rowX = 3
    return rowX


buttons = StringVar()
print(type(buttons))

#This creates the board and the buttons and runs the game

for x in range(0,9):
    button= "button"+str(x)
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

    
    button = Button(tk, text= " ", height = 4, width = 8, command=lambda j=x:turnChecker(j))
    button.grid(row = rowXI, column = columnX, sticky = S+N+E+W)
    allbuttons.append(button)


tk.mainloop()
