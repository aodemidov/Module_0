#!/usr/bin/env python
# coding: utf-8

# # Проект 0. GitHub. Самый быстрый старт 
# ### Итоговое задание Демидова А. О. Поток DSPR-59

# ## Приветствие

def welcome():
    print(' Добро пожаловать в игр "Угадай число"! ')
    print(' Цель игры - отгадать загаддное от 1 до 100 число ')
    while True:
        mode = input(' Отгадывать число будете Вы (1) или компьютер (0)? ')
        
        if not(mode.isdigit()):
            print(" Введите 1 или 0! ")
            continue
        
        n = int(mode)
        
        if not(n in [0,1]):
            print(" Введите 1 или 0! ")
            continue
        return mode


# ## Кто загадывает число?

def ask():
    while True:
        mode = input(' Хотите загадать число сами (1) или доверимся случайному выбору(0)? ')
        
        if not(mode.isdigit()):
            print(" Введите 1 или 0! ")
            continue
        
        n = int(mode)
        
        if not(n in [0,1]):
            print(" Введите 1 или 0! ")
            continue
        return mode


# ## Пользовательская игра

def game_user(number):
    count = 0
    while True:
        number_user = input(' Введите предполагаемое число: ')
        
        if not(number_user.isdigit()):
            print(' Введите число! ')
            continue
        
        number_user = int(number_user)
        if number_user < 1 or number_user > 100:
            print( 'Введите число в диапазоне от 1 до 100! ')
            continue
        
        count += 1
        if number_user < number:
            print(f' Число {number_user} меньше загаданного')
            print(' Попробуйте ещё раз! ')
            continue
            
        if number_user > number:
            print(f' Число {number_user} больше загаданного')
            print(' Попробуйте ещё раз! ')
            continue
        return count


# ## Игра компьютера

def game_computer(number):
    count = 0
    top_number = 100
    low_number = 0
    number_computer = 50
    while True:
        count += 1
        print(f' Попытка {count}, текущее число: {number_computer}')
        
        if number_computer == number:
            return count
        
        low_number = number_computer if number_computer < number else low_number
        top_number = number_computer if number_computer > number else top_number
        number_computer = int((top_number + low_number)/2)      


# ## Текст выигрыша

def text_win(count,player):
    if player == 'user':
        player = 'Вы угадали'
    else:
        player = 'Компьютер угадал'
    
    if count%10 == 1 and count != 11:
        return f' {player} число за {count} попытку! '
    elif 1 < count%10 < 5 and (count > 15 or count < 5) :
        return f' {player} число за {count} попытки! '
    else:
        return f' {player} число за {count} попыток! ' 


# # Игра

get_ipython().system('pip install numpy')
import numpy as np
mode = int(welcome())
if mode == 1:
    number = np.random.randint(1,101)
    count = game_user(number)
    print(text_win(count,'user'))
else:
    var = ask()
    if var == 1:
        while True:
            number = input(' Введите число от 1 до 100: ')
            
            if not(number.isdigit()):
                print(' Введите число! ')
                continue
            
            number = int(number)
            
            if number < 1 or number > 100:
                print(' Введите число в диапазоне от 1 до 100! ')
                continue
            break
        count = game_computer(number)
        print(text_win(count,'computer'))
    else:
        number = np.random.randint(1,101)
        print(f' Случайным образом загадано число {number}')
        count = game_computer(number)
        print(text_win(count,'computer'))