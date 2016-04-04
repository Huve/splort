#!/usr/bin/python
#
# April 3 2016

import pygame
from pygame.locals import *
import game_screen
import sys

class Game():
    """Game class that stores what is occurring during the game."""
    def __init__(self):
        self.screen = game_screen.GameScreen()
        self.bg = self.screen.draw_background()
        self.start_game()

    def start_game(self):
        print "game started"

    def run(self):
        while 1:
            for event in pygame.event.get():
                if hasattr(event, 'key'):
                    if event.key == K_ESCAPE:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit(0)

            
        
        
