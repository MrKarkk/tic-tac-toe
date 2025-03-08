import random
from colorama import Fore, Style

def make_move(row, col, player):
    if 1 <= row <= 3 and 1 <= col <= 3:
        if arr_play[row][col] == '-': 
            arr_play[row][col] = player
            return True
        else:
            print("Ячейка уже занята!")
            return False
    else:
        print("Неверные координаты!")
        return False

def check_winner():
    for row in range(1, 4): # Проверка строк
        if arr_play[row][1] == arr_play[row][2] == arr_play[row][3] != '-':
            return arr_play[row][1]
    
    for col in range(1, 4): # Проверка столбцов
        if arr_play[1][col] == arr_play[2][col] == arr_play[3][col] != '-':
            return arr_play[1][col]
    
    if arr_play[1][1] == arr_play[2][2] == arr_play[3][3] != '-': # Проверка диагоналей
        return arr_play[1][1]
    
    if arr_play[1][3] == arr_play[2][2] == arr_play[3][1] != '-':
        return arr_play[1][3]
    
    return None

def print_board():
    for i in range(1, 4): # Печатаем обновленное поле без скобок и запятых
        row_str = ''
        for j in range(1, 4):
            cell = arr_play[i][j]
            if cell == 'X':
                row_str += Fore.GREEN + cell + Style.RESET_ALL  # Зеленый цвет для X
            elif cell == 'O':
                row_str += Fore.RED + cell + Style.RESET_ALL  # Красный цвет для O
            else:
                row_str += cell  # Для пустых ячеек
            if j < 3:
                row_str += ' | '  # Разделитель столбцов
        print(row_str)
        if i < 3:
            print("-" * 9)  # Разделитель строк

arr_play = [[0, 1, 2, 3], 
            [1, '-', '-', '-'], 
            [2, '-', '-', '-'], 
            [3, '-', '-', '-']]

turns = 0
while turns < 9:
    print_board()
    
    if turns % 2 == 0:
        print("\nВаш ход!")
        abc = int(input("Введите координаты: "))
        abc_1 = abc // 10  
        abc_2 = abc % 10   
        if make_move(abc_1, abc_2, "X"):
            turns += 1
    else:
        while True:  # Случайный ход для O, пока не будет найдено свободное место
            print("\nХодит игрок 'O'!")
            abc_1, abc_2 = random.randint(1, 3), random.randint(1, 3)
            if make_move(abc_1, abc_2, "O"):
                turns += 1
                break

    winner = check_winner()
    if winner:
        print_board()
        print(f"\nИгрок {winner} выиграл!")
        break

    print("\n" + "-" * 20)  

else:
    print("\nНичья!")