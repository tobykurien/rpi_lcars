import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen


class ScreenAuthorize(LcarsScreen):

    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_2.png"),
                        layer=0)

        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "AUTHORIZATION REQUIRED", 2),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (330, -1), "ONLY AUTHORIZED PERSONNEL MAY ACCESS THIS TERMINAL", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (360, -1), "TOUCH TERMINAL TO PROCEED", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (390, -1), "FAILED ATTEMPTS WILL BE REPORTED", 1.5),
                        layer=1)

        all_sprites.add(LcarsGifImage("assets/gadgets/stlogorotating.gif", (103, 369), 50), layer=1)        

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        Sound("assets/audio/enter_authorization_code.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/206.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny1 = Sound("assets/audio/deny_1.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        self.attempts = 0
        self.granted = False

    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.attempts > 1):
                self.granted = True
                self.sound_beep1.play()
            else:
                if self.attempts == 0: self.sound_deny1.play()
                else: self.sound_deny2.play()
                self.granted = False
                self.attempts += 1

        if event.type == pygame.MOUSEBUTTONUP:
            if (self.granted):
                self.sound_granted.play()
                from screens.main import ScreenMain
                self.loadScreen(ScreenMain())
            else:
                self.sound_denied.play()
        

        return False
