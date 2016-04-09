#!/usr/bin/python
#
# April 3 2016

import random
import ground_block

class RegionMap():
    """A map of a region within the game."""
    def __init__(self, screen, game, display, map_data=None):
        self.w = display.Info().current_w
        self.h = display.Info().current_h
        self.game = game
        self.screen = screen
        self.tiles = ["a",
                      "b",
                      "c",
                      "d"
            ]
        self.region = self.generate_region(map_data)


    def generate_region(self, map_data):
        """Generates the region of a map.

        Args:
            map_data: data from a pre-defined map.

        Returns:
            region: dictionary of tile image locations.
        """
        ground_blocks = []
        x = y = 0
        if map_data == None:
            #region = {
                #i:{j:self.tiles[random.randint(0, len(self.tiles)-1)] for j in range(100)} for i in range(200)
                #}
            region = [
            ]
            for _ in range(100):
                row = ""
                for _ in range(100):
                    i = random.choice(self.tiles)
                    row += i
                    g = ground_block.GroundBlock(i, x, y)
                    ground_blocks.append(g)
                    self.screen.entities.add(g)
                    x+=64
                y+=64
                x=0
                region.append(row)
        else:
            pass
        self.game.ground_blocks = ground_blocks
        return region


    def get_tiles(self, pixel_coord):
        """Provides the tiles that should be shown on the screen.

        Args:
            coord: tuple of coordinates the player exists on.

        Returns:
            view: the tiles that should be displayed on the screen by pixel.
        """
            
        view = {}
        for i in range(self.w / self.screen.tile_size + 2):
            for j in range(self.h / self.screen.tile_size + 2):
                x = i + (pixel_coord[0] / self.screen.tile_size) - 9
                y = j + (pixel_coord[1] / self.screen.tile_size) - 7
                try:
                    view[i][j] = self.region[x][y]
                except KeyError:
                    view[i] = {}
                    view[i][j] = self.region[x][y]
        return view

        
