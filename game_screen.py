#!/usr/bin/python
#
# April 3 2016

import pygame
import region_map

class GameScreen():
    """Game Screen class that acts as a View for the user"""
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 768))
        self.draw_background()
        pygame.display.flip()

    def draw_background(self):
        self.bg = region_map.RegionMap()
        for i in range(16):
            for j in range(12):
                tile = pygame.image.load('images/' + self.bg.tiles[i][j] + '.png')
                self.screen.blit(tile, (i*64,j*64))

    def draw_player(self, coord):
        pass

    def draw_title_screen(self):
        pass
