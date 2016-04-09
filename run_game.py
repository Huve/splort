#!/usr/bin/python
#
# April 3 2016

import splort_game

    
if __name__ == "__main__":

    WIDTH = 1088
    HEIGHT = 768
    HALF_WIDTH = WIDTH/2
    HALF_HEIGHT = HEIGHT/2
    
    FLAGS = 0
    DEPTH = 32
    
    game = splort_game.Game(WIDTH, HEIGHT)
    game.run()
