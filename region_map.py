#!/usr/bin/python
#
# April 3 2016

import random

class RegionMap():
    """A map of a region within the game."""
    def __init__(self, screen, display, map_data=None):
        self.w = display.Info().current_w
        self.h = display.Info().current_h
        self.screen = screen
        self.tiles = ["dirt_1",
                      "grass_1"
            ]
        self.region = self.generate_region(map_data)


    def generate_region(self, map_data):
        """Generates the region of a map.

        Args:
            map_data: data from a pre-defined map.

        Returns:
            region: dictionary of tile image locations.
        """
        if map_data == None:
            region = {
                i:{j:self.tiles[random.randint(0, len(self.tiles)-1)] for j in range(100)} for i in range(100)
                }
        else:
            pass
        return region

    def get_tiles(self, pixel_coord):
        """Returns the tiles that should be shown on the screen.

        Args:
            coord: tuple of coordinates the player exists on.

        Returns:
            view: the tiles that should be displayed on the screen by pixel.
        """
        view = {}
        for i in range(self.w / self.screen.tile_size + 2):
            for j in range(self.w / self.screen.tile_size + 2):
                x = i + (pixel_coord[0] / self.screen.tile_size) - 9
                y = j + (pixel_coord[1] / self.screen.tile_size) - 7
                try:
                    view[i][j] = self.region[x][y]
                except KeyError:
                    view[i] = {}
                    view[i][j] = self.region[x][y]
        return view

        
