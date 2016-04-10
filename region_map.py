#!/usr/bin/python
#
# April 3 2016

import random
from ground_block import GroundBlock, Block

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
                      "d"]
        self.blocks = ["1",
                       " ", " ", " ", " ", " ", " ",
                       "2"]
        self.region = self.generate_region(map_data)
        self.layer_1 = self.generate_block_layer(None)


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
            region = []
            for _ in range(100):
                row = ""
                for _ in range(100):
                    i = random.choice(self.tiles)
                    row += i
                    g = GroundBlock(i, x, y)
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


    def generate_block_layer(self, block_data):
        blocks = []
        x = y = 0
        if block_data == None:
            region = []
            for _ in range(100):
                row = ""
                for _ in range(100):
                    i = random.choice(self.blocks)
                    row += i
                    if i != " ":
                        b = Block(i, x, y)
                        blocks.append(b)
                        self.screen.entity_layer_1.add(b)
                    x+=64
                y+=64
                x=0
                region.append(row)
        else:
            pass
        self.game.blocks = blocks
        return region

        
