#!/usr/bin/python
#
# April 3 2016

import pygame

class GameScreen():
    """Game Screen class that acts as a View for the user"""
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 768))
        self.draw_background()
        pygame.display.flip()

    def draw_background(self):
        self.bg = pygame.image.load("images/background_1.png")
        self.screen.blit(self.bg, (0,0))

    def draw_title_screen(self):
        pass
