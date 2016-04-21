from ui.utils.gif_image import GIFImage
from ui.widgets.sprite import LcarsWidget

class LcarsGifImage(LcarsWidget):
    
    def __init__(self, imagefilename, pos, duration=-1):
        self.image = GIFImage(imagefilename, duration)
        self.pos = pos
        size = (self.image.get_rect().width, self.image.get_rect().height)
        LcarsWidget.__init__(self, None, pos, size)
        
    def update(self, screen):
        if self.visible:
            self.image.render(screen, self.rect)
