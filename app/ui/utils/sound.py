"""Helper classes and functions needed to globally enable/disable sound"""
import pygame
from pygame.mixer import Sound as OldSound

import config

# Cannot use inheritance or decorator because pygame.mixer.Sound is a C-extension.
class Sound:
    """Class wrapping ``pygame.mixer.Sound`` with the ability to enable/disable sound globally

    Use this instead of ``pygame.mixer.Sound``. The interface is fully transparent.
    """
    def __init__(self, source):
        if config.SOUND:
            self.sound = OldSound(source)

    def play(self, loops=0, maxtime=0, fade_ms=0):
        if config.SOUND:
            self.sound.play(loops, maxtime, fade_ms)

    def stop(self):
        if config.SOUND:
            self.sound.stop()

    def fadeout(self, time):
        if config.SOUND:
            self.sound.fadeout(time)

    def set_volume(self, value):
        if config.SOUND:
            self.sound.set_volume(value)

    def get_volume(self):
        if config.SOUND:
            return self.sound.get_volume()

    def get_num_channels(self):
        if config.SOUND:
            return self.sound.get_num_channels()

    def get_length(self):
        if config.SOUND:
            return self.get_length()

    def get_raw(self):
        if config.SOUND:
            return self.sound.get_raw()


def init(audio_params):
    """Use this instead of ``pygame.mixer.init``"""
    if config.SOUND:
        pygame.mixer.init(audio_params[0], audio_params[1], audio_params[2], audio_params[3])
