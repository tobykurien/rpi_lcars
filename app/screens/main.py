from datetime import datetime

from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

from datasources.network import get_ip_address_string
from pathlib import Path


class ScreenMain(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_1.png"),
                        layer=0)
                        
        self.beep1 = Sound("assets/audio/panel/201.wav")

        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (15, 44), "BINANCE"),
                        layer=1)
                        
        all_sprites.add(LcarsText(colours.ORANGE, (5, 140), "TRADING BOT", 2),
                        layer=1)

        self.ip_address = LcarsText(colours.BLACK, (444, 520),
                                    get_ip_address_string())
        all_sprites.add(self.ip_address, layer=1)

        # date display
        self.stardate = LcarsText(colours.BLUE, (15, 510), "TIME", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # buttons
        all_sprites.add(LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler),
                        layer=4)
        
        # wallet-balance
        self.balance = LcarsText(colours.PURPLE, (15, 330), "USDT", 1.5)
        all_sprites.add(self.balance , layer=1)
        
        # last 13 log-lines        
        self.logline1 = LcarsText(colours.ORANGE, (110, 130), "", 1.2)
        self.logline2 = LcarsText(colours.ORANGE, (135, 130), "", 1.2)
        self.logline3 = LcarsText(colours.ORANGE, (160, 130), "", 1.2)
        self.logline4 = LcarsText(colours.ORANGE, (185, 130), "", 1.2)
        self.logline5 = LcarsText(colours.ORANGE, (210, 130), "", 1.2)
        self.logline6 = LcarsText(colours.ORANGE, (235, 130), "", 1.2)
        self.logline7 = LcarsText(colours.ORANGE, (260, 130), "", 1.2)
        self.logline8 = LcarsText(colours.ORANGE, (285, 130), "", 1.2)
        self.logline9 = LcarsText(colours.ORANGE, (310, 130), "", 1.2)
        self.logline10 = LcarsText(colours.ORANGE, (335, 130), "", 1.2)
        self.logline11 = LcarsText(colours.ORANGE, (360, 130), "", 1.2)
        self.logline12 = LcarsText(colours.ORANGE, (385, 130), "", 1.2)
        self.logline13 = LcarsText(colours.ORANGE, (410, 130), "", 1.2)
        
        all_sprites.add(self.logline1 , layer=1)
        all_sprites.add(self.logline2 , layer=1)
        all_sprites.add(self.logline3 , layer=1)
        all_sprites.add(self.logline4 , layer=1)
        all_sprites.add(self.logline5 , layer=1)
        all_sprites.add(self.logline6 , layer=1)
        all_sprites.add(self.logline7 , layer=1)
        all_sprites.add(self.logline8 , layer=1)
        all_sprites.add(self.logline9 , layer=1)
        all_sprites.add(self.logline10 , layer=1)
        all_sprites.add(self.logline11 , layer=1)
        all_sprites.add(self.logline12 , layer=1)
        all_sprites.add(self.logline13 , layer=1)
        
        
    def tail(filename, n=1):
        with open(filename, "r") as f:
            lines = f.readlines()
            return "\n".join(lines[-n:])

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("{}".format(datetime.now().strftime("%d/%m  %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
            self.balance.setText("USDT: " + Path('/home/pi/Binance-volatility-trading-bot/balance-script/balance.txt').read_text().splitlines()[-1] + " $")
            self.logline1.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-1])
            self.logline2.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-2])
            self.logline3.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-3])
            self.logline4.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-4])
            self.logline5.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-5])
            self.logline6.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-6])
            self.logline7.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-7])
            self.logline8.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-8])
            self.logline9.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-9])
            self.logline10.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-10])
            self.logline11.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-11])
            self.logline12.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-12])
            self.logline13.setText(Path('/home/pi/Binance-volatility-trading-bot/bvtb_1/trades.txt').read_text().splitlines()[-13])
        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    def hideInfoText(self):
        if self.info_text[0].visible:
            for sprite in self.info_text:
                sprite.visible = False

    def showInfoText(self):
        for sprite in self.info_text:
            sprite.visible = True

    def gaugesHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = True
        self.weather.visible = False

    def sensorsHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = True
        self.dashboard.visible = False
        self.weather.visible = False

    def weatherHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = True

    def homeHandler(self, item, event, clock):
        self.showInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = False
        
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())


