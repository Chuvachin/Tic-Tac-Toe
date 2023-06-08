import random
import pygame
pygame.init()
wanna_play = True
pygame.mixer.music.load('Ineffable Mysteries - Shpongle.mp3')
pygame.mixer.music.play()
#pole = [" "," "," "," "," "," "," "," "," "]
def print_board(board):
    print()
    print(board[0] , '|' , board[1] , '|' , board[2])
    print('__|___|__')
    print(board[3] , '|' , board[4] , '|' , board[5])
    print('__|___|__')
    print(board[6] , '|' , board[7] , '|' , board[8])
    print('  |   |  ')
    print()
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def get_result():
    win = ""
 
    for i in victories:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            win = "X"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            win = "O"   
             
    return win



def check_line(sum_O,sum_X):
 
    step = " "
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0,3):
            if pole[line[j]] == "O":
                o = o + 1
            if pole[line[j]] == "X":
                #ТУТ МЫ ПРОВЕРЯЕМ ЛИНИИ НА СООТВЕТСТВИ ПРОКРУТКЕ В АИ (КОЛИЧЕСТВО НОЛИКОВ И КРЕСТИКОВВ КАЖДОЙ, ПРИЧЕМ БЕЗ КОНКРЕТИКИ
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if pole[line[j]] != "O" and pole[line[j]] != "X":
                    step = line[j] #А ТУТ ИЩЕМ В СТРОЧКЕ КОНКРЕТИКУ, ТО ЕСТЬ ДЫРУ, ГДЕ НИХУЯ НЕТУ, ЧТО ЗАПОЛНИТЬ ЕЕ!!!
    return step

def players_hod():
    global pole#это возможность изменять поле)
    while True:
        try:
            cell= int(input('куда ебашим? \n'))-1
            if cell in range(0,9):
                if pole[cell]==' ':
                    pole[cell]='X'
                    break
                # -1 bc count from 0
        except ValueError:
            pass
        print('АААААААААААААААА Я ТЕБЯ ЗАХУЯРЮ')
    print("ti hodid ")#не ты, а твой
    print_board(pole)
def easy_mod():
    global pole
    while True:
        cell=random.randint(0,8)
        if pole[cell]==' ':
            pole[cell]='O'
            break
    print("Computer hodid ")
    print_board(pole)
def hard_mod():
    global pole
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
 
    # 5) если центр занят, то занимаем первую ячейку
    while step == " ":
        if step == " ":
            corn = random.choice([0,2,6,8])
            if pole[corn] != "X" and pole[corn] != "O":
                step = corn

    pole[step]="O"
    print("Computer hodid ")
    print_board(pole)
while wanna_play: #это все равно что вхиле труе
    pole = [" "," "," "," "," "," "," "," "," "]
    print_board([1,2,3,4,5,6,7,8,9])
    lvl = input("choose difficulty: easy/hard \n").lower()
    while lvl!="easy" and lvl!="hard":   
        print("Пиши нормально, дебил, дурак, читать не умеешь?")
        lvl = input("choose difficulty: easy/hard \n").lower()
    while True:
        try:
            hod = int(input("каким ходить будешшшш ? 1/2 \n"))
            if hod==1 or hod==2:
                break
        except ValueError:
            pass#вот это мы не ебем че такое, но надо
        print("Ты пришибленый или как? ты цифр не знаешь? ты дурак.")
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
            print("nichia")
            break
    wanna_play = input("Wanna play?Yes/NO GOD PLEASE NO \n").upper()   
    while wanna_play!="YES" and wanna_play!="NO":
        print("я 10 раз спрашивать... буду конечно, но ты не ахуел, либуж?")
        wanna_play = input("Wanna play?Yes/NO GOD PLEASE NO \n").upper()
        
    if wanna_play == "NO":
        exit()
