from pygame import Rect
from run_game import WIDTH, HEIGHT, HALF_WIDTH, HALF_HEIGHT

class Camera(object):
    """A camera that follows a sprite."""
    def __init__(self, function, w, h):
        self.function = function
        self.state = Rect(0, 0, w, h)
        
        
    def apply(self, target):
        """Applies the camera to a target to blit all objects on the screen.
        
        Args:
            target: sprite (e.g., player, block, etc.) which camera is to be applied to.
            
        Returns:
            position and size of the object on the screen.
        """
        return target.rect.move(self.state.topleft)
        
        
    def update(self, target):
        """Updates the camera's location based on center target (i.e., the player).
        
        Args:
            target: the sprite object of the target to be watched.
            
        Returns:
            updates the state of the camera based on a rectangle returned by camera function used.
        """
        self.state = self.function(self.state, target.rect)

        
def simple_camera(camera, target_rect):
    """Defines a simple camera to follow a sprite.
    
    Args:
        camera: camera which will use the function.
        target_rect: Rect of the character to be followed.
        
    Returns:
        Rectangle of the location and dimensions of the camera: Rect(l, t, w, h)
    """
    l, t, _, _ = target_rect
    _, _, w, h = camera      
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)
  
  
def complex_camera(camera, target_rect):
    """Defines a complex camera to follow a sprite limited by the edges of the map.
    
    Args:
        camera: camera which will use the function.
        target_rect: Rect of the character to be followed.
        
    Returns:
        Rectangle of the location and dimensions of the camera: Rect(l, t, w, h)
    """
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h
    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIDTH), l)        # stop scrolling at the right edge
    t = max(-(camera.height-HEIGHT), t)        # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)