#!/usr/bin/python
#
# April 3 2016

import pygame
from pygame.locals import *
import game_screen
import sys
import player

class Game():
    """Game class that stores what is occurring during the game."""
    def __init__(self, w, h):
        pygame.init()
        self.player = player.Player(0,0)
        self.screen = game_screen.GameScreen(self, pygame.display, self.player, w, h)
        self.coord = self.screen.coord
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.right = False
        self.running = False
        self.ground_blocks = []
        
    def update_coord(self, coord):
        self.coord = coord
        self.screen.coord = coord
        self.screen.draw_layers()
    
    def run(self):
        while 1:
           # keys = pygame.key.get_pressed()
           # if keys[pygame.K_RIGHT]:
           #     self.right=True
           # if keys[pygame.K_LEFT]:
            #    self.left=True
           # if keys[pygame.K_UP]:
           #     self.up=True
          #  if keys[pygame.K_DOWN]:
           #     self.down=True
            for e in pygame.event.get():
           #     if hasattr(event, 'key'):
           #         keys = pygame.key.get_pressed()
           #         if event.key == K_ESCAPE:
           #             pygame.display.quit()
           #             pygame.quit()
           #             sys.exit(0)
                if e.type == QUIT: raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit, "ESCAPE"
                if e.type == KEYDOWN and e.key == K_UP:
                    self.up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    self.down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    self.left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    self.right = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    self.running = True

                if e.type == KEYUP and e.key == K_UP:
                    self.up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    self.down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    self.right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    self.left = False
            self.player.update(self.up, self.down, self.left, self.right, self.running, self.ground_blocks)
            self.screen.draw_layers() 

            
        
        
