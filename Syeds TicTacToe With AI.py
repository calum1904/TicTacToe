#Imports Random
import random
###########################################################################
#Board and board layout
board=[0,1,2,3,4,5,6,7,8]
print(board[0],'|', board[1],'|', board[2])
print('---------')
print(board[3],'|', board[4],'|', board[5])
print('---------')
print(board[6],'|', board[7],'|', board[8])
##################################################################
def show():
        print(board[0],'|', board[1],'|', board[2])
        print('---------')
        print(board[3],'|', board[4],'|', board[5])
        print('---------')
        print(board[6],'|', board[7],'|', board[8])
##################################################################
        #Checks lines in 3 spots and returns true
def checkLine (char, spot1, spot2, spot3):
    if board [spot1]==char and board[spot2]==char and board[spot3]==char:
        return True
###############################################################################
    #Different combinations to win using checkline
def checkAll(char):
    if checkLine(char,0,1,2):
        return True
    if checkLine(char,1,4,7):
        return True
    if checkLine(char,2,5,8):
        return True

    if checkLine(char,6,7,8):
        return True
    if checkLine(char,3,4,5):
        return True
    if checkLine(char,1,2,3):
        return True
    
    if checkLine(char,2,4,6):
        return True
    if checkLine(char,0,4,8):
        return True

#The gameworks
    #user selects spot if the board doesnt have values x or o it replaces it with either
    #x or o dependant on turn
while True:
    UsersChoice = int(input("Select a spot"))
    if board[UsersChoice] != 'X' and board[UsersChoice] != 'O':
        board[UsersChoice] = 'X'
        checkAll("X")
        finding = True
        while finding == True:
            random.seed()
            opponent = random.randint(0,8)
            if board[opponent] != 'O' and board[opponent] != 'X':
                board[opponent] = 'O'
                checkAll("O")
                finding = False
 
            show()
    else:
        print("This spot is taken!")
