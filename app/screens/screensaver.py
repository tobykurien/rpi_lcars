import sys
import pygame
import config
import globalvars

from datetime import datetime

from ui import colours
from ui.utils.sound import Sound
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen
from ui.widgets.lcars_widgets import LcarsButton

class ScreenSaver(LcarsScreen):

    def setup(self, all_sprites):

        #if config.DEV_MODE:
        #    all_sprites.add(LcarsButton(colours.GREY_BLUE, (0, 770), "X", self.exitHandler, (30, 30)), layer=2)
        
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_screensaver.png"),
                        layer=0)
        
        # add screen blanking here
        # for example turn off RPi display backlight
        pass

    def update(self, screenSurface, fpsClock):
        pass

    def handleEvents(self, event, fpsClock):
        #self.sound_beep1.play()
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #if event.type == pygame.MOUSEBUTTONUP:
        #    from screens.main import ScreenMain
        #    self.loadScreen(ScreenMain())
        if event.type:
            globalvars.lastEventTime = datetime.now().timestamp() + config.SCREENSAVERTIME
            self.returnScreen()
        return False

    #def exitHandler(self, item, event, clock):
    #    sys.exit()
