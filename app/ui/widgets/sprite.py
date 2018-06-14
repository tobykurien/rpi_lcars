import pygame
from ui.utils.interpolator import Interpolator

class LcarsWidget(pygame.sprite.DirtySprite):
    """Base class for all widgets"""

    def __init__(self, color, pos, size, handler=None):
        pygame.sprite.DirtySprite.__init__(self)
        if self.image == None:
            self.image = pygame.Surface(size).convert()
            self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.top = pos[0]
        self.rect.left = pos[1]
        self.size = (self.rect.width, self.rect.height)

        self.long_pressed = False
        self.pressed_time = 0            
        self.focussed = False
        self.line = None
        self.handler = handler

    def update(self, screen):
        if not self.visible:
            return
        
        if self.line != None:
            self.line.next()
            if self.rect.center == self.line.pos:
                self.dirty = 0
                
            self.rect.center = self.line.pos
        else:
            self.dirty = 0

        screen.blit(self.image, self.rect)

    def handleEvent(self, event, clock):
        handled = False
        if not self.visible:
            self.focussed = False
            return handled
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pressed_time = pygame.time.get_ticks()
            self.focussed = True
                
        if event.type == pygame.MOUSEMOTION:
            if (self.focussed and pygame.time.get_ticks() - self.pressed_time > 1000):
                self.long_pressed = True
                if self.groups()[0].UI_PLACEMENT_MODE:
                    self.rect.top = event.pos[1]
                    self.rect.left = event.pos[0]
                    self.dirty = 1            

        if event.type == pygame.MOUSEBUTTONUP:
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
            if self.focussed and self.long_pressed and self.groups()[0].UI_PLACEMENT_MODE:
                print(event.pos[1], event.pos[0])
                
            self.pressed_time = 0
            self.long_pressed = False
            self.focussed = False
                
        return handled

    def applyColour(self, colour):
        """Convert non-black areas of an image to specified colour"""
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                pixel = self.image.get_at((x, y)).r
                if (pixel > 50):
                    self.image.set_at((x, y), colour)

class LcarsMoveToMouse(LcarsWidget):
    """For testing purposes - move a small square to last clicked position"""
    def __init__(self, color):
        self.image = None
        LcarsWidget.__init__(self, color, (0,0), (10,10))
        self.focussed = True

    def handleEvent(self, event, clock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # move sprite to clicked location using interpolator
            fps = clock.get_fps()
            x, y = event.pos
            
            self.line = Interpolator(
                self.rect.center,
                (x, y),
                0.5, # duration of interpolation
                fps, # current frames per second
                1.0, # type of interpolation
                0.5  # middle?
            )
            
            self.dirty = 1
    
