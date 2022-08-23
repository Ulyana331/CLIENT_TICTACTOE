import pygame
import os
import events
import actions
import socket

from win_condition import check_win

list_krest = list()
list_nolik = list()
                 #012
list_map = [list('000'),#0
            list('000'),#1
            list('000')]#2

IP = '54.161.100.228'
PORT = 55556

def connection():
    global list_map
    try:
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((IP,PORT))
        list_map = str(list_map)
        connection.send(list_map.encode('utf8'))
        list_map = connection.recv(1024).decode('utf8')
        list_map = eval(list_map)
    except:
        pass

def run():
    global list_map
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    map = os.path.join(os.path.abspath(__file__+'/..')+'/Images/','TicTacToe_MAP.png')
    pygame.display.set_caption('TiCtAcToE')
    map = pygame.image.load(map)
    map = pygame.transform.scale(map,(600,600))
    fps = pygame.time.Clock()
    game = True
    X=0
    Y=0
    flag_move = True
    
    while game:
        print(list_map)
        game = check_win(list_map,game)
        screen.blit(map,(0,0))
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        
        if pressed[0] and flag_move == True:
            if pos[0]>=0 and pos[0] <200 and pos[1]>=0 and pos[1] <200 and list_map[0][0]=='0':
                list_map[0][0] = '1'
            if pos[0]>=200 and pos[0]<400 and pos[1] >= 200 and pos[1] <400 and list_map[1][1] == '0':
                list_map[1][1] = '1'
            if pos[0]>=400 and pos[0] <=600 and pos[1] >=400 and pos[1] <=600 and list_map[2][2] == '0':
                list_map[2][2] = '1'
            if pos[0] >= 200 and pos[0] <400 and pos[1]>=0 and pos[1] <200 and list_map[0][1] == '0':
                list_map[0][1] = '1'
            if pos[0] >= 400 and pos[0] <600 and pos[1]>=0 and pos[1] <200 and list_map[0][2] == '0':
                list_map[0][2] = '1'
            if pos[0]>=0 and pos[0]<200 and pos[1] >= 200 and pos[1] <400 and list_map[1][0] == '0':
                list_map[1][0] = '1'
            if pos[0]>=400 and pos[0]<600 and pos[1] >= 200 and pos[1] <400 and list_map[1][2] == '0':
                list_map[1][2] = '1'
            if pos[0]>=200 and pos[0] <=400 and pos[1] >=400 and pos[1] <=600 and list_map[2][1] == '0':
                list_map[2][1] = '1'
            if pos[0]>=0 and pos[0] <=200 and pos[1] >=400 and pos[1] <=600 and list_map[2][0]== '0':
                list_map[2][0] = '1'
            
        for i in list_map:
            for n in i:
                if n == '1':
                    krest = actions.KrestXNolik(X,Y,200,200,'krest.png')
                    list_krest.append(krest)
                if n == '3':
                    nolik = actions.KrestXNolik(X,Y,200,200,'nolik.png')
                    list_nolik.append(nolik)
                X+=200
            X=0
            Y+=200
        Y = 0
        for x in list_nolik:
            x.show_krestXnolik(screen)
        for y in list_krest:
            y.show_krestXnolik(screen)
        
        pygame.display.flip()
        fps.tick(30)
        connection()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = False

run()

