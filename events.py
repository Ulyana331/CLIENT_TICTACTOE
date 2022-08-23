import pygame
import sys
def exit():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

