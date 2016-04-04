#!/usr/bin/python
#
# April 3 2016

import splort_game

def run_game():
    """Runs the Splort game."""
    game = splort_game.Game()
    game.run()
    print "Game running."

def main():
    run_game()
    
if __name__ == "__main__":
    main()
