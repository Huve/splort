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
        self.player = player.Player(1599,1500)
        self.screen = game_screen.GameScreen(self, pygame.display, self.player, w, h)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.right = False
        self.running = False
        self.ground_blocks = []
        self.collision_layer =[]
        
    def run(self):
        while 1:
            for e in pygame.event.get():
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
            self.player.update(self.up, self.down, self.left, self.right, self.running, self.ground_blocks, self.collision_layer)
            self.screen.draw_layers() 

            
        
        
