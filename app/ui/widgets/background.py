from ui.widgets.sprite import LcarsWidget
import pygame

class LcarsBackground(LcarsWidget):
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsBackgroundImage(LcarsWidget):
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        LcarsWidget.__init__(self, None, (0,0), None)
    
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsImage(LcarsWidget):
    def __init__(self, image, pos):
        self.image = pygame.image.load(image).convert()
        LcarsWidget.__init__(self, None, pos, None)
