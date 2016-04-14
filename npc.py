
from player import Entity
import pygame
import random

class NPC(Entity):

    """An entity that acts as an NPC on the map."""
    def __init__(self, race, x, y):
        Entity.__init__(self)
        self.image_map = {
            "a":"images/char_paladin_2.png"}
        self.animation_key = {
            "up": 0,
            "right": 1,
            "down": 2,
            "left": 3
            }
        self.images = []
        self.sprite_sheet = pygame.image.load(self.image_map[race])
        self.load_walk_animation()
        self.direction = "up"
        self.rect = pygame.Rect(x, y, 64, 64)
        self.hostile = False
        self.health = 10
        self.mana = 10
        self.index = 0
        self.fps = 5
        self.frame_count = 0

        
    def update(self):
        """Update the sprite's location and animations."""
        images = self.images[self.animation_key[self.direction]]
        self.frame_count +=1
        if self.frame_count % self.fps == 0:
            self.index += 1
            if self.index >= len(images):
                self.index = 0
            self.image = images[self.index]
            if self.frame_count > 10000:
                self.frame_count = 0
                
                
    def load_walk_animation(self):
        """Load the walking animations from the sprite sheet."""
        sheet_dim = self.sprite_sheet.get_rect().size
        cols = sheet_dim[0] / 64
        rows = sheet_dim[1] / 64
        for r in range(rows):
            image_row = []
            for c in range(cols):
                self.sprite_sheet.set_clip(pygame.Rect(c*64, r*64, 64 ,64))
                image = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip())
                image.convert()
                image_row.append(image)
            self.images.append(image_row)
        self.image = self.images[0][0]
        
        
