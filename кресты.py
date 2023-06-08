#import pygame
#pygame.init()
#pygame.mixer.music.load('Ineffable Mysteries - Shpongle.mp3')
#pygame.mixer.music.play()

import random

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_board(board):
    print()
    print(board[0] , '|' , board[1] , '|' , board[2])
    print('__|___|__')
    print(board[3] , '|' , board[4] , '|' , board[5])
    print('__|___|__')
    print(board[6] , '|' , board[7] , '|' , board[8])
    print('  |   |  ')
    print()
    

def get_result(): #проверка на выигрышную комбинации (с любой стороны)
    win = ""
 
    for i in victories:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            win = "X"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            win = "O"   

    return win

def players_hod():
    print("Your turn")
    while True: # тобы не заыершилась при вводе НЕцифры
        try:
            cell= int(input('Enter cell number \n'))-1
            if cell in range(0,9):
                if pole[cell]==' ':
                    pole[cell]='X'
                    break
        except ValueError:
            pass
        print('Something went wrong, try again')
    print_board(pole)

def easy_mod():
    while True:
        cell=random.randint(0,8)
        if pole[cell]==' ':
            pole[cell]='O'
            break
    print("Computers turn")
    print_board(pole)
    
def check_line(sum_O,sum_X): #считаем количество фигур на стоках (часть хард мод ф-ции)
 
    step = " "
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0,3):
            if pole[line[j]] == "O":
                o = o + 1
            if pole[line[j]] == "X":
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if pole[line[j]] != "O" and pole[line[j]] != "X":
                    step = line[j] 
    return step

def hard_mod():
    step = " "
 
    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2,0)
 
    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == " ":
        step = check_line(0,2) 
    # 3) если 1 фигура своя и 0 чужих - ставим
    if step == " ":
        step = check_line(1,0)
 
    # 4) центр пуст, то занимаем центр
    if step == " ":
        if pole[4] != "X" and pole[4] != "O":
            step = 4
 
    # 5) если центр занят, то занимаем угловую ячейку
    while step == " ":
        if step == " ":
            corn = random.choice([0,2,6,8])
            if pole[corn] != "X" and pole[corn] != "O":
                step = corn

    pole[step]="O"
    print("Computers tern")
    print_board(pole)
wanna_play = True
while wanna_play: 
    pole = [" "," "," "," "," "," "," "," "," "]
    print_board([1,2,3,4,5,6,7,8,9])
    lvl = input("Choose difficulty: easy/hard \n").lower()
    while lvl!="easy" and lvl!="hard":   
        print("Something went wrong, try again ")
        lvl = input("Choose difficulty: easy/hard \n").lower()
    while True:
        try:
            hod = int(input("Will you take a first or a second tern? (1/2) \n"))
            if hod==1 or hod==2:
                break
        except ValueError:
            pass
        print("Something went wrong, try again")
    while True:
        count=0
        if hod == 1:
            players_hod()
        else:
            if lvl == "easy":
                easy_mod()
            else:
                hard_mod()
        if hod == 1:
            hod=2
        else:
            hod=1
        if get_result() == "X":
            print("Player win")
            break
        if get_result() == "O":
            print("Computer win")
            break
        for t in pole:
            if t==" ":
                break
            count+=1
        if count == 9:
            print("Draw")
            break
    wanna_play = input("Wanna playagain? (Yes/No) \n").upper()   
    while wanna_play!="YES" and wanna_play!="NO":
        print("Something went wrong, try again")
        wanna_play = input("Wanna play again? (Yes/No) \n").upper()
        
    if wanna_play == "NO":
        exit()

    

          
            
    
        


