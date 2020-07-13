import sys
import pygame
import config

from ui import colours
from ui.utils.sound import Sound
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen
from ui.widgets.lcars_widgets import LcarsButton

class ScreenAuthorize(LcarsScreen):

    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_2.png"),
                        layer=0)

        all_sprites.add(LcarsGifImage("assets/gadgets/stlogorotating.gif", (103, 369), 50), 
                        layer=0)        

        all_sprites.add(LcarsText(colours.ORANGE, (270, -1), "AUTHORIZATION REQUIRED", 2),
                        layer=0)

        all_sprites.add(LcarsText(colours.BLUE, (330, -1), "ONLY AUTHORIZED PERSONNEL MAY ACCESS THIS TERMINAL", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (360, -1), "TOUCH TERMINAL TO PROCEED", 1.5),
                        layer=1)
        
        #all_sprites.add(LcarsText(colours.BLUE, (390, -1), "FAILED ATTEMPTS WILL BE REPORTED", 1.5),layer=1)


        all_sprites.add(LcarsButton(colours.GREY_BLUE, (320, 60), "1", self.num_1), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (370, 60), "2", self.num_2), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (320, 200), "3", self.num_3), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (370, 200), "4", self.num_4), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (320, 340), "5", self.num_5), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (370, 340), "6", self.num_6), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (320, 480), "7", self.num_7), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (370, 480), "8", self.num_8), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (320, 610), "9", self.num_9), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (370, 610), "0", self.num_0), layer=2)

        if config.DEV_MODE:
            all_sprites.add(LcarsButton(colours.GREY_BLUE, (0, 770), "X", self.exitHandler, (30, 30)), layer=2)
        
        self.layer1 = all_sprites.get_sprites_from_layer(1)
        self.layer2 = all_sprites.get_sprites_from_layer(2)

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/201.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny1 = Sound("assets/audio/deny_1.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        self.reset()

    def reset(self):
        # Variables for PIN code verification
        self.correct = 0
        self.pin_i = 0
        self.granted = False
        for sprite in self.layer1: sprite.visible = True
        for sprite in self.layer2: sprite.visible = False

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play sound
            self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            if (not self.layer2[0].visible):
                for sprite in self.layer1: sprite.visible = False
                for sprite in self.layer2: sprite.visible = True
                Sound("assets/audio/enter_authorization_code.wav").play()
            elif (self.pin_i == len(str(config.PIN))):
                # Ran out of button presses
                if (self.correct == len(config.PIN)):
                    self.sound_granted.play()
                    from screens.main import ScreenMain
                    self.loadScreen(ScreenMain())
                else:
                    self.sound_deny2.play()
                    self.sound_denied.play()
                    self.reset()

        return False

    def num_1(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '1':
            self.correct += 1

        self.pin_i += 1

    def num_2(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '2':
            self.correct += 1

        self.pin_i += 1

    def num_3(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '3':
            self.correct += 1

        self.pin_i += 1

    def num_4(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '4':
            self.correct += 1

        self.pin_i += 1

    def num_5(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '5':
            self.correct += 1

        self.pin_i += 1

    def num_6(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '6':
            self.correct += 1

        self.pin_i += 1

    def num_7(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '7':
            self.correct += 1

        self.pin_i += 1

    def num_8(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '8':
            self.correct += 1

        self.pin_i += 1

    def num_9(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '9':
            self.correct += 1

        self.pin_i += 1

    def num_0(self, item, event, clock):
        if str(config.PIN)[self.pin_i] == '0':
            self.correct += 1

        self.pin_i += 1

    def exitHandler(self, item, event, clock):
        sys.exit()
