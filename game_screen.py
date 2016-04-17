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
        self.players = pygame.sprite.Group()
        self.entity_layer_1 = pygame.sprite.Group()
        self.entity_layer_2 = pygame.sprite.Group()
        self.screen = display.set_mode((w, h))
        self.bg = pygame.image.load("images/background.png").convert()
        self.total_width = self.bg.get_rect().size[0]
        self.total_height = self.bg.get_rect().size[1]
        self.region = region_map.RegionMap(self, game, self.display)
        self.camera = camera.Camera(complex_camera, self.total_width, self.total_height)
        self.player = player
        self.player.image = self.display_player(self.player, "images/m_char2.png")
        self.players.add(player)
        self.draw_layers()
        pygame.display.flip()
       
    
    def draw_layers(self):
        self.camera.update(self.player)
        self.screen.blit(self.bg, (self.camera.state[0], self.camera.state[1]))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        for e in self.entity_layer_1:
           e.update()
           self.screen.blit(e.image, self.camera.apply(e))
        pygame.display.update()
        
        
    def display_player(self, player, image):
        image = pygame.image.load(image)
        image.convert()
        return image


    def animate_sprite(self, sprite, image):
        pass