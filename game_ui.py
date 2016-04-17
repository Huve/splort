import pygame
class GameUI():
    def __init__(self, display, player):
        self.w = display.Info().current_w
        self.h = display.Info().current_h
        self.layer = pygame.Surface((self.w, self.h))
        self.layer.set_colorkey((0,0,0))
        self.layer.set_alpha(175)
        red = (255,0,0)
        blue = (0,50,255)
        self.health = 100
        self.mana = 100
        pygame.draw.rect(self.layer, red, (20, 20, self.health, 20))
        pygame.draw.rect(self.layer, blue, (20, 50, self.mana, 20))
        
        
    def update(self):
        self.layer.draw.rect()