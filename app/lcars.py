from screens.authorize import ScreenAuthorize
from ui import UI

# global config
UI_PLACEMENT_MODE = True
RESOLUTION = (800, 480)
FPS = 60
DEV_MODE = True

ui = UI(ScreenAuthorize(), RESOLUTION, UI_PLACEMENT_MODE, FPS, DEV_MODE)
while (True):
    ui.tick()
