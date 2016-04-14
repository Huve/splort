from player import Entity
import pygame

class GroundBlock(Entity):
    """An entity that acts as a ground tile on the map."""
    def __init__(self, a, x, y):
        Entity.__init__(self)
        self.image_map = {
        "a":"images/dirt_2.png",
        "b":"images/grass_6.png",
        "c":"images/grass_6.png",
        "d":"images/grass_6.png"}
        
        self.image = pygame.Surface((64, 64))
        self.image.convert()
        self.image = pygame.image.load(self.image_map[a])
        self.rect = pygame.Rect(x, y, 64, 64)

    def update(self):
        pass
        
class Block(Entity):
    """An entity that acts as a first layer (collision layer) tile on the map."""
    def __init__(self, a, x, y):
        Entity.__init__(self)
        self.image_map = {
        "1":"images/tree_2.png",
        "2":"images/bush_1.png"
        }
        #self.image = pygame.Surface((64, 64))
        self.image = pygame.image.load(self.image_map[a])
        self.image.convert()
        self.rect = pygame.Rect(x, y, 64, 64)

    def update(self):
        pass
        