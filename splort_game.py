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
        pygame.mixer.init()
        self.player = player.Player(1500,1500)
        self.screen = game_screen.GameScreen(self, pygame.display, self.player, w, h)
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.right = False
        self.running = False
        self.direction = None
        self.current_press = None
        self.layer_1 = self.screen.entity_layer_1
        self.layer_2 = self.screen.entity_layer_2
        self.intro_music = "audio/splort_2.mp3"
        pygame.mixer.music.load(self.intro_music)
        pygame.mixer.music.play()
        
    def run(self):
        while 1:
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit, "ESCAPE"
                if e.type == KEYDOWN and e.key == K_UP:
                    self.direction = "up"
                if e.type == KEYDOWN and e.key == K_DOWN:
                    self.direction = "down"
                if e.type == KEYDOWN and e.key == K_LEFT:
                    self.direction = "left"
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    self.direction = "right"
                if e.type == KEYDOWN and e.key == K_SPACE:
                    self.running = True

                if e.type == KEYUP:
                    if e.key == K_UP or e.key == K_DOWN or e.key == K_LEFT or e.key == K_RIGHT:
                        self.direction = None
            self.player.update(self.direction, self.layer_1)
            self.screen.draw_layers() 

            
        
        
