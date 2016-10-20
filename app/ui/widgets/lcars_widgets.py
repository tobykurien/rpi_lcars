import pygame
from pygame.font import Font
from pygame.locals import *
from pygame.mixer import Sound

from ui.widgets.sprite import LcarsWidget
from ui import colours

class LcarsButton(LcarsWidget):
    def __init__(self, colour, shape, pos, text, handler=None):
        self.handler = handler

        # Load different image for shape
        if (shape == "rect"):
            image = pygame.image.load("assets/rectangle.png").convert()
        elif (shape == "rounded"):
            image = pygame.image.load("assets/button.png").convert()

        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 22)
        textImage = font.render(text, False, colours.BLACK)

        # Change text position
        if (shape == "rect"):
            image.blit(textImage,
                   (image.get_rect().width - textImage.get_rect().width - 18,
                    image.get_rect().height - textImage.get_rect().height - 12))
        elif (shape == "rounded"):
            image.blit(textImage,
                   (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False

        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True

        LcarsWidget.handleEvent(self, event, clock)
        return handled

class LcarsText(LcarsWidget):
    def __init__(self, colour, pos, message, size=1.0, background=None):
        self.colour = colour
        self.background = background
        self.font = Font("assets/swiss911.ttf", int(19.0 * size))

        self.renderText(message)
        # center the text if needed
        if (pos[1] < 0):
            pos = (pos[0], 400 - self.image.get_rect().width / 2)

        LcarsWidget.__init__(self, colour, pos, None)

    def renderText(self, message):
        if (self.background == None):
            self.image = self.font.render(message, True, self.colour)
        else:
            self.image = self.font.render(message, True, self.colour, self.background)

    def setText(self, newText):
        self.renderText(newText)
