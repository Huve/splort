from pygame import Rect

class Camera(object):
    def __init__(self, function, w, h):
        self.function = function
        self.state = Rect(10, 0, w, h)
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.function(self.state, target.rect)

        
def simple_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera      
        return Rect(-l+500, -t+389, w, h)