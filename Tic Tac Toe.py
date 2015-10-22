#Calum's TicTacToe code using Tkinter to make a GUI
#The label dosn't work as it is supposed to change with playersTurn but it dosn't

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
        playersTurn = "O"
        if (allbuttons[0]["text"] == "X" and allbuttons[1]["text"] == "X" and allbuttons[2]["text"] == "X" or
                allbuttons[3]["text"] == "X" and allbuttons[4]["text"] == "X" and allbuttons[5]["text"] == "X" or
                allbuttons[6]["text"] == "X" and allbuttons[7]["text"] == "X" and allbuttons[8]["text"] == "X" or
                allbuttons[0]["text"] == "X" and allbuttons[3]["text"] == "X" and allbuttons[6]["text"] == "X" or
                allbuttons[1]["text"] == "X" and allbuttons[4]["text"] == "X" and allbuttons[7]["text"] == "X" or
                allbuttons[2]["text"] == "X" and allbuttons[5]["text"] == "X" and allbuttons[8]["text"] == "X" or
                allbuttons[0]["text"] == "X" and allbuttons[4]["text"] == "X" and allbuttons[8]["text"] == "X" or
                allbuttons[2]["text"] == "X" and allbuttons[4]["text"] == "X" and allbuttons[6]["text"] == "X"):
                playAgain = tkinter.messagebox.askyesno("WINNER", "The winner is X! \n Would you like to play again?")
                if playAgain is True:
                    reset()
                elif playAgain is False:
                    tk.destroy()
                    
        

    elif playersTurn == "O":
        playersTurn = "X"
        if (allbuttons[0]["text"] == "O" and allbuttons[1]["text"] == "O" and allbuttons[2]["text"] == "O" or
                allbuttons[3]["text"] == "O" and allbuttons[4]["text"] == "O" and allbuttons[5]["text"] == "O" or
                allbuttons[6]["text"] == "O" and allbuttons[7]["text"] == "O" and allbuttons[8]["text"] == "O" or
                allbuttons[0]["text"] == "O" and allbuttons[3]["text"] == "O" and allbuttons[6]["text"] == "O" or
                allbuttons[1]["text"] == "O" and allbuttons[4]["text"] == "O" and allbuttons[7]["text"] == "O" or
                allbuttons[2]["text"] == "O" and allbuttons[5]["text"] == "O" and allbuttons[8]["text"] == "O" or
                allbuttons[0]["text"] == "O" and allbuttons[4]["text"] == "O" and allbuttons[8]["text"] == "O" or
                allbuttons[2]["text"] == "O" and allbuttons[4]["text"] == "O" and allbuttons[6]["text"] == "O"):
                playAgain = tkinter.messagebox.askyesno("WINNER", "The winner is O! \n Would you like to play again?")
                if playAgain is True:
                    reset()
                elif playAgain is False:
                    tk.destroy()
        
def reset():
    for x in range(0,9):
        allbuttons[x]["text"] = " "
            
#This function checks whos turn it is and wether or not they can click that box
def turnChecker(button):
    print( button )
    
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
