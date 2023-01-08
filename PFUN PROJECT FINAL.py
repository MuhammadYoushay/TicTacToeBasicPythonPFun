#PFUN PROJECT 2021--------TIC-TAC-TOE GAME---------GROUP MEMBERS (MUHAMMAD YOUSHAY, SIKANDER AHMED, KUSHAL CHANDANI)

#WE ADDED THIS GUI TO OUR CODE USING HELP FROM THE INTERNET 
from tkinter import *
#CREATE WINDOW OBJECT
window = Tk() #GENERATING THE POP-UP WINDOW

#DEFINE LABELS 
l1 = Label(window, text = "WELCOME TO THE TIC TAC TOE GAME! \n CLOSE THIS TAB TO START THE GAME!")
l1.grid(row = 0, column = 0)#TO CREATE A SINGLE WINDOW

window.mainloop()#MONITOR KEY CLICKS/MOUSE CLICKS ETC

#MAIN PROGRAM'S CODE

#INITIALIZING THE BOARD USING NESTED LISTS
board = [[" " for col in range(4)]for row in range(4)]  #CREATING A MATRIX
win = False
#"PLAYER" IS A LIST OF TWO INTEGERS WHICH REPRESENTS PLAYER 1 AND PLAYER 2
player = [1, 2]
#"TURN" IS A LIST WITH TWO STRINGS WHICH REPRESENTS THE "O" & "X" -CIRCLE AND CROSS USED IN TIC-TAC-TOE
turn = ["O","X"]
#"MOVES" IS A VARIABLE TO KEEP A COUNTER OF THE NUMBER OF MOVES
moves= 0
#"CHECK" IS A COUNTER WE ARE USING TO CHECK OUR CONDITIONS OF WINNING, LOSING AND A POSSIBLE TIE
check = 0
#MAIN PROGRAM STARTS FROM HERE
while not(win):
    #WE ARE CREATING A GRID HERE TO MAKE OUR BOARD LOOK MORE REALISTIC
    for row in range(1, 4):
        for col in range(1, 4):
            print(board[row][col], end="")
            if col != 3:
                print("|", end="")
        if row != 3:
            print()
            print("-|-|-")
    print ()
    #PLAYER 1 WILL ENTER THE ROW AND COLUMN IN WHICH HE WANTS TO ENTER "O"-CIRCLE
    print("Player",player[0])
    r = int(input("Enter Row"))
    c = int(input("Enter Col"))
    #HERE WE ARE CHECKING IF THE ROW AND COLUMN ENTERED BY PLAYER 1 ARE EMPTY OR NOT, IF A PREVIOUS VALUE IS FOUND, WE'LL END THE GAME WITH AN ERROR MESSAGE
    if board[r][c]==" ":
        board[r][c] = turn[0]
    else:
        print("ERROR! You can't choose a box(row,col) which has already been taken by the other player. You are violating the game rules. We can no longer allow you to play")
        exit()
    #HERE WE ARE INCREMENTING THE MOVES BY 1 AS PLAYER 1 HAS MADE THE FIRST MOVE
    moves = moves +1
    #HERE WE ARE CHECKING FOR A POSSIBLE WIN
    for row in range(1, 4):
        for col in range(1, 4):
            if board[row][col]=="O":
                check = check+1
            else:
                    check=0
                #IF CHECK BECOMES 3, IT MEANS THAT PLAYER 1 HAS WON THE GAME
        if check==3:
            win=True
    if win == True:
        break
    #PRINTING THE WINNING BOARD
    for col in range(1, 4):
        for row in range(1, 4):
            if board[row][col] == "O":
                 check = check + 1
            else:
                 check = 0
        if check == 3:
            win = True
            for row in range(1, 4):
                for col in range(1, 4):
                    print(board[row][col], end="")
                    if col != 3:
                        print("|", end="")
                if row != 3:
                    print()
                    print("-|-|-")
            print ()

            print("Congragulations! Player 1 wins!!!")
            break
    check=0
    if win == True:
        break
#CHECKING DIAGNOLLY FOR A WIN FOR PLAYER 1

    if board[1][1]=="O" and board[2][2]=="O" and board[3][3]=="O":
        check=1
    elif board[1][3]=="O" and board[2][2]=="O" and board[3][1]=="O":
        check=1
    else:
        check=0
    if check==1:
        win= True
        #PRINTING THE WINNING BOARD
        for row in range(1, 4):
                for col in range(1, 4):
                    print(board[row][col], end="")
                    if col != 3:
                        print("|", end="")
                if row != 3:
                    print()
                    print("-|-|-")
        print ()
        print("Congragulations! Player 1 wins!!!")
        break
#CHECKING FOR A POSSIBLE TIE
    if moves == 9 and win==False:
        #PRINTING THE FINAL BOARD
        for row in range(1, 4):
                for col in range(1, 4):
                    print(board[row][col], end="")
                    if col != 3:
                        print("|", end="")
                if row != 3:
                    print()
                    print("-|-|-")
        print ()
        print("Match has ended in a Draw. Good to see how competitive both players are!")
        break
    for row in range(1, 4):
        for col in range(1, 4):
            print(board[row][col], end="")
            if col != 3:
                print("|", end="")
        if row != 3:
           print()
           print("-|-|-")
    print()
    #TAKING INPUTS FROM PLAYER 2
    print("Player",player[1])
    r= int(input("Enter Row"))
    c=int(input("Enter Column"))
    if board[r][c]==" ":
        board[r][c]=turn[1]
    else:
        print("ERROR! You can't choose a box(row,col) which has already been taken by the other player. You are violating the game rules. We can no longer allow you to play")
        exit()
    moves = moves +1
#FOR PLAYER TWO, WE WILL INCREMENT THE CHECK BY 2 TO DIFFERENTIATE THE CODE OF PLAYER 1 AND PLAYER 2, REST REMAINS THE SAME 
    for row in range(1, 4):
        for col in range(1, 4):
            if board[row][col]=="X":
                check = check+2
            else:
                check=0
            if check==6:
                win=True
                for row in range(1 ,4):
                    for col in range(1, 4):
                        print(board[row][col], end="")
                        if col != 3:
                            print("|", end="")
                    if row != 3:
                        print()
                        print("-|-|-")
                print ()
                print("Congragulations! Player 2 wins!!!")
                break
        check=0
        if win ==True:
            break
    for col in range(1, 4):
        for row in range(1, 4):
            if board[row][col]=="X":
                check=check +2
            else:
                check=0
        if check==6:
            win=True
            for row in range(1, 4):
                for col in range(1, 4):
                    print(board[row][col], end="")
                    if col != 3:
                        print("|", end="")
                if row != 3:
                    print()
                    print("-|-|-")
            print ()
            print("Congragulations! Player 2 wins!!!")
            break
    check = 0
    if win == True:
        break
    if board[1][1]=="X" and board[2][2]=="X" and board[3][3]=="X":
        check=2
    elif board[1][3]=="X" and board[2][2]=="X" and board[3][1]=="X":
        check=2
    else:
        check=0
    if check ==2:
        win = True
        for row in range(1, 4):
                for col in range(1, 4):
                    print(board[row][col], end="")
                    if col != 3:
                        print("|", end="")
                if row != 3:
                    print()
                    print("-|-|-")
        print ()
        print("Congragulations! Player 2 wins!!!")
        break
#-----------------------------------------------------------------------PROGRAM END-------------------------------------------------------------------------------
