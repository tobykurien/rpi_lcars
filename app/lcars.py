from screens.main import ScreenMain
from ui.ui import UserInterface
import config

if __name__ == "__main__":
    firstScreen = ScreenMain()
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
                       config.SOUND)

    while (True):
        ui.tick()
