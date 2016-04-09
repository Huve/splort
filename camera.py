from pygame import Rect

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
    return Rect(-l+544, -t+379, w, h)
  
  
def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+544, -t+379, w, h
    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-1088), l)        # stop scrolling at the right edge
    t = max(-(camera.height-768), t)        # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)