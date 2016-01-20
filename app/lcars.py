import pygame, sys
from pygame.locals import *
from screens.authorize import ScreenAuthorize
from screens.main import ScreenMain

# global config
UI_PLACEMENT_MODE = False
RESOLUTION = (800, 480)
FPS = 60
DEV_MODE = False

# init system
pygame.mixer.init(22050, -8, 1, 1024)
pygame.font.init()
pygame.init()

screenSurface = pygame.display.set_mode(RESOLUTION) #, pygame.FULLSCREEN)
fpsClock = pygame.time.Clock()
pygame.display.set_caption("LCARS")
if not DEV_MODE: pygame.mouse.set_visible(False)

# set up screen elements
all_sprites = pygame.sprite.LayeredDirty()
all_sprites.UI_PLACEMENT_MODE = UI_PLACEMENT_MODE

screen = ScreenAuthorize()
screen.setup(all_sprites)

def update():
    screen.update(fpsClock)
    all_sprites.update(screenSurface)
    pygame.display.update()

def handleEvents():
    global screen
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or \
            (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            return

        for sprite in all_sprites.sprites():
            if hasattr(event, "pos"):
                focussed = sprite.rect.collidepoint(event.pos)
                if (focussed or sprite.focussed) and sprite.handleEvent(event, fpsClock):
                    break
            
        screen.handleEvents(event, fpsClock)

        newScreen = screen.getNextScreen()
        if (newScreen):
            all_sprites.empty()
            newScreen.setup(all_sprites)
            screen = newScreen
            break
    
while pygame.display.get_init():
    update()
    handleEvents()
    fpsClock.tick(FPS)
