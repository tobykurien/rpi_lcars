import pygame
from pygame.locals import *

class UserInterface:
    def __init__(self, screen, resolution=(800,480), 
                 ui_placement_mode=False, fps=60, dev_mode=False,
                 audio=(22050, -8, 1, 1024)):
        # init system
        pygame.mixer.init(audio[0], audio[1], audio[2], audio[3])
        pygame.font.init()
        pygame.init()
        
        self.screenSurface = pygame.display.set_mode(resolution) #, pygame.FULLSCREEN)
        self.fpsClock = pygame.time.Clock()
        self.fps = fps
        pygame.display.set_caption("LCARS")
        if not dev_mode: 
            # see https://github.com/tobykurien/rpi_lcars/issues/9
            #pygame.mouse.set_visible(False)
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        
        # set up screen elements
        self.all_sprites = pygame.sprite.LayeredDirty()
        self.all_sprites.UI_PLACEMENT_MODE = ui_placement_mode
    
        self.screen = screen
        self.screen.setup(self.all_sprites)
        self.running = True

    def update(self):
        self.screen.pre_update(self.screenSurface, self.fpsClock)
        self.all_sprites.update(self.screenSurface)
        self.screen.update(self.screenSurface, self.fpsClock)
        pygame.display.update()
    
    def handleEvents(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
                (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                self.running = False
                return
    
            for sprite in self.all_sprites.sprites():
                if hasattr(event, "pos"):
                    focussed = sprite.rect.collidepoint(event.pos)
                    if (focussed or sprite.focussed) and sprite.handleEvent(event, self.fpsClock):
                        break
                
            self.screen.handleEvents(event, self.fpsClock)
    
            newScreen = self.screen.getNextScreen()
            if (newScreen):
                self.all_sprites.empty()
                newScreen.setup(self.all_sprites)
                self.screen = newScreen
                break
    
    def isRunning(self):
        pygame.display.get_init()
    
    def tick(self):
        self.update()
        self.handleEvents()
        self.fpsClock.tick(self.fps)
