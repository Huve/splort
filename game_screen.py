#!/usr/bin/python
#
# April 3 2016

import camera
from camera import complex_camera
from camera import simple_camera
import pygame
import region_map

class GameScreen():
    """Game Screen class that acts as a View for the user"""
    def __init__(self, game, display, player, w, h):
        self.tile_size = 64
        self.game = game
        self.display = display
        self.entities = pygame.sprite.Group()
        self.screen = display.set_mode((w, h))
        self.region = region_map.RegionMap(self, game, self.display)
        self.camera = camera.Camera(complex_camera, 
            len(self.region.region[0])*self.tile_size, 
            len(self.region.region)*self.tile_size)
        self.player = player
        self.player.image = pygame.image.load('images/m_char.png')
        self.player.image.convert()
        self.entities.add(player)
        self.draw_layers()
        pygame.display.flip()
       
    
    def draw_layers(self):
        self.camera.update(self.player)
        for e in self.entities:
            self.screen.blit(e.image, self.camera.apply(e))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        pygame.display.flip()
        pygame.display.update()


