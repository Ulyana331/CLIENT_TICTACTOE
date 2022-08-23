import pygame   
import os 
class KrestXNolik():
    def __init__(self,X,Y,WIDTH,HEIGHT,IMAGE):
        self.X = X
        self.Y = Y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.IMAGE = os.path.join(os.path.abspath(__file__+'/..')+'/Images/',IMAGE)
        self.IMAGE = pygame.image.load(self.IMAGE)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
    def show_krestXnolik(self,screen):
        screen.blit(self.IMAGE,(self.X,self.Y))

