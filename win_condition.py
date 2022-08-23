import pygame 


def check_win(list_map,game):
    game = True
    if list_map[0][0] == '1' and list_map[0][1] == '1' and list_map[0][2] == '1':
        print('Победа Крестики')
        game = False
    elif list_map[0][0] == '3' and list_map[0][1] == '3' and list_map[0][2] == '3':
        print('Победа Нолики ')
    elif list_map[1][0] == '1' and list_map[1][1] == '1' and list_map[1][2] == '1': 
        print('Победа Крестики')
    elif list_map[1][0] == '3' and list_map[1][1] == '3' and list_map[1][2] == '3':
        print('Победа Нолики ')
    elif list_map[2][0] == '3' and list_map[2][1] == '3' and list_map[2][2] == '3':
        print('Победа Нолики ')
    elif list_map[2][0] == '1' and list_map[2][1] == '1' and list_map[2][2] == '1':
        print('Победа Крестики')
    elif list_map[0][0] == '3' and list_map[1][1] == '3' and list_map[2][2] == '3':
        print('Победа Крестики')
    elif list_map[0][0] == '3' and list_map[1][1] == '3' and list_map[2][2] == '3':
        print('Победа Нолики ')
    elif list_map[0][2] == '1' and list_map[1][1] == '1' and list_map[2][0] == '1':
        print('Победа Крестики')
    elif list_map[0][2] == '3' and list_map[1][1] == '3' and list_map[2][0] == '3':
        print('Победа Нолики ')
    elif list_map[0][0] == '1' and list_map[1][0] == '1' and list_map[2][0] == '1':
        print('Победа Крестики')
    elif list_map[0][0] == '3' and list_map[1][0] == '3' and list_map[2][0] == '3':
        print('Победа Нолики ')
    elif list_map[0][1] == '1' and list_map[1][1] == '1' and list_map[2][1] == '1':
        print('Победа Крестики')
    elif list_map[0][1] == '3' and list_map[1][1] == '3' and list_map[2][1] == '3':
        print('Победа Нолики ')
    elif list_map[0][2] == '1' and list_map[1][2] == '1' and list_map[2][2] == '1':
        print('Победа Крестики')
    elif list_map[0][2] == '3' and list_map[1][2] == '3' and list_map[2][2] == '3':   
        print('Победа Нолики ')
    return game