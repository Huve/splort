#!/usr/bin/python
#
# April 3 2016

import pygame
import region_map

class GameScreen():
    """Game Screen class that acts as a View for the user"""
    def __init__(self, display):
        self.tile_size = 64
        self.display = display
        self.screen = display.set_mode((1088, 768))
        self.coord = (3000,5000)
        self.draw_background(self.coord)
        self.player_image = pygame.image.load('images/m_char.png')
        self.draw_layers()
        pygame.display.flip()
        

    def draw_background(self, coord):
        """Draws the background for the game."""
        self.region_map = region_map.RegionMap(self, self.display)
        self.view = self.region_map.get_tiles(coord)
        w = self.region_map.w / self.tile_size + 1
        h = self.region_map.h / self.tile_size + 1
        wr = float(coord[0]) % self.tile_size
        hr = float(coord[1]) % self.tile_size
        for i in range(0, w + 1):
            for j in range(0, h + 1):
                tile = pygame.image.load("images/" + self.view[i][j] + ".png")
                self.screen.blit(tile, (-self.tile_size + i * self.tile_size + wr,
                                        -self.tile_size + j * self.tile_size + hr)
                                 )


    def draw_player(self, coord=(512, 352)):
        """Draws the player in the center.

        Args:
            coord: pixel coordinates of the player.
        """
        self.screen.blit(self.player_image, coord)

    def draw_title_screen(self):
        pass

    def draw_layers(self):
        self.draw_background(self.coord)
        self.draw_player()
