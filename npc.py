
from player import Entity
import pygame
import random

class NPC(Entity):

    """An entity that acts as an NPC on the map."""
    def __init__(self, a, x, y):
        Entity.__init__(self)
        self.image_map = {
        "3":"images/char_paladin_1.png"}
        self.sprite_sheet = pygame.image.load(self.image_map[a])
        self.sprite_sheet.set_clip(pygame.Rect(0, 0, 64 ,64))
        self.image_1 = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip()) 
        self.sprite_sheet.set_clip(pygame.Rect(64, 0, 64 ,64))
        self.image_2 = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip()) 
        self.sprite_sheet.set_clip(pygame.Rect(128, 0, 64 ,64))
        self.image_3 = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip()) 
        self.sprite_sheet.set_clip(pygame.Rect(192, 0, 64 ,64))
        self.image_4 = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip()) 
        self.images = [self.image_1, self.image_2, self.image_3, self.image_4]
        self.image = self.images[random.randint(0, 1)]
        self.image.convert()
        self.rect = pygame.Rect(x, y, 64, 64)
        self.hostile = False
        self.health = 10
        self.mana = 10
        self.index = 0
        self.fps = 5
        self.frame_count = 0

    def update(self):
        self.frame_count +=1
        if self.frame_count % self.fps == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            if self.frame_count > 10000:
                self.frame_count = 0
