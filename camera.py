from pygame import Rect
from run_game import WIDTH, HEIGHT, HALF_WIDTH, HALF_HEIGHT

class Camera(object):
    def __init__(self, function, w, h):
        self.function = function
        self.state = Rect(0, 0, w, h)
        
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
        
        
    def update(self, target):
        self.state = self.function(self.state, target.rect)

        
def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera      
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)
  
  
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h
    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIDTH), l)        # stop scrolling at the right edge
    t = max(-(camera.height-HEIGHT), t)        # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)