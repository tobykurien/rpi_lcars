import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton
from ui.widgets.screen import LcarsScreen

class ScreenAuthorize(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_splash.png"), layer=0)
        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "AUTHORIZATION REQUIRED", 2), layer=1)
        all_sprites.add(LcarsGifImage("assets/gadgets/stlogorotating.gif", (103, 369), 50), layer=1)

        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (320, 130), "1", self.num_1), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (370, 130), "2", self.num_2), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (320, 270), "3", self.num_3), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (370, 270), "4", self.num_4), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (320, 410), "5", self.num_5), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (370, 410), "6", self.num_6), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (320, 550), "7", self.num_7), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, "btn", (370, 550), "8", self.num_8), layer=2)

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        Sound("assets/audio/enter_authorization_code.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/206.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        ############
        # SET PIN CODE WITH THIS VARIABLE
        ############
        self.pin = 1234
        ############

        # Variables for PIN code verification
        self.correct = 0
        self.pin_i = 0
        self.granted = False

    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play sound
            self.sound_beep1.play()

            # Print debug
            print(self.pin_i, str(self.pin)[self.pin_i], self.correct)

        if event.type == pygame.MOUSEBUTTONUP:
            if (self.pin_i == len(str(self.pin))):
                # Ran out of button presses
                if (self.correct == 4):
                    self.sound_granted.play()
                    from screens.main import ScreenMain
                    self.loadScreen(ScreenMain())
                else:
                    self.sound_deny2.play()
                    self.sound_denied.play()
                    from screens.idle import ScreenIdle
                    self.loadScreen(ScreenIdle())

        return False

    def num_1(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '1':
            self.correct += 1

        self.pin_i += 1

    def num_2(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '2':
            self.correct += 1

        self.pin_i += 1

    def num_3(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '3':
            self.correct += 1

        self.pin_i += 1

    def num_4(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '4':
            self.correct += 1

        self.pin_i += 1

    def num_5(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '5':
            self.correct += 1

        self.pin_i += 1

    def num_6(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '6':
            self.correct += 1

        self.pin_i += 1

    def num_7(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '7':
            self.correct += 1

        self.pin_i += 1

    def num_8(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '8':
            self.correct += 1

        self.pin_i += 1
