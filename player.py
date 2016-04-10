#!/usr/bin/python
#
# April 3 2016
import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
class Player(Entity):

    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.rect = pygame.Rect(x, y, 64, 64)
        
        
    def update(self, up, down, left, right, running, platforms, layer_1):
        if up:
            self.yvel = -2
        if down:
            self.yvel = 2
        if running:
            self.xvel = 2
        if left:
            self.xvel = -2
        if right:
            self.xvel = 2
        if not(left or right or up or down):
            self.xvel = 0
            self.yvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        # self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        #self.collide(0, self.yvel, platforms)

        
    """def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom"""