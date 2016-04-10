#!/usr/bin/python
#
# April 3 2016
import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
class Player(Entity):
    """Player class Entity."""
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.rect = pygame.Rect(x, y, 64, 64)
        self.player_class = ""
        self.health = 10
        self.mana = 10
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        
        
    def update(self, direction, layer_1):
        """Update the player's position.
        
        Args:
            up: boolean referring to keypress up.
            down: boolean referring to keypress down.
            left: boolean referring to keypress left.
            right: boolean referring to keypress right.
            running: boolean referring to spacebar press.
            layer_1: list of sprites that player can collide with
        """
        if direction == "up":
            self.yvel = -2
            self.xvel = 0
        if direction == "down":
            self.yvel = 2
            self.xvel = 0
        if direction == "left":
            self.xvel = -2
            self.yvel = 0
        if direction == "right":
            self.xvel = 2
            self.yvel = 0
        if direction not in ("right", "left", "up", "down"):
            self.xvel = 0
            self.yvel = 0
        self.rect.left += self.xvel
        self.rect.top += self.yvel
        self.collide(self.xvel, 0, layer_1)
        self.collide(0, self.yvel, layer_1)

        
    def collide(self, xvel, yvel, layer_1):
        """Determine if player is colliding with objects
        
        Args:
            xvel: speed on x axis.
            yvel: speed on y axis.
            layer_1: list of sprites that player can collide with.
        """
        for p in layer_1:
            if pygame.sprite.collide_rect(self, p):
               # if isinstance(p, GroundBlock):
                   # pass  # TODO(huve): add doors to this ExitBlock
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.top = p.rect.bottom