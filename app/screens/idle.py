import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen

class ScreenIdle(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_splash.png"), layer=0)
        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "AUTHORIZATION REQUIRED", 2), layer=1)
        all_sprites.add(LcarsText(colours.BLUE, (330, -1), "ONLY AUTHORIZED PERSONNEL MAY ACCESS THIS TERMINAL", 1.5), layer=1)
        all_sprites.add(LcarsText(colours.BLUE, (360, -1), "TOUCH TERMINAL TO PROCEED", 1.5), layer=1)
        all_sprites.add(LcarsGifImage("assets/gadgets/stlogorotating.gif", (103, 369), 50), layer=1)

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        self.sound_beep1 = Sound("assets/audio/panel/206.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny1 = Sound("assets/audio/deny_1.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        self.granted = False

    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)

        if event.type == pygame.MOUSEBUTTONDOWN:
                self.granted = True
                self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            if (self.granted):
                #self.sound_granted.play()
                from screens.authorize import ScreenAuthorize
                self.loadScreen(ScreenAuthorize())

        return False
