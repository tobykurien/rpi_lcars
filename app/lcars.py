from screens.authorize import ScreenAuthorize
from ui.ui import UserInterface
import config

# global config
#UI_PLACEMENT_MODE = True
#RESOLUTION = (800, 480)
# RESOLUTION = (1366, 768)
#FPS = 60
#DEV_MODE = True

if __name__ == "__main__":
    firstScreen = ScreenAuthorize()
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE)

    while (True):
        ui.tick()
