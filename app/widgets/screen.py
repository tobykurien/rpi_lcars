import pygame
class LcarsScreen:
    """
    Manage a UI screen
    """
    def __init__(self):
        self.nextScreen = None
        self.lastFrameTicks = 0
    
    def setup(self):
        pass

    def getDeltaTime(self, fpsClock):
        """
        Return the amount of time in milliseconds since last frame 
        """
        t = pygame.time.get_ticks()
        deltaTime = (t - self.lastFrameTicks)
        self.lastFrameTicks = t
        return deltaTime
    
    def update(self, fpsClock):
        """
        Called every frame to run any UI updates 
        """
        pass
    
    def handleEvents(self, event, fpsClock):
        """
        Called when an event occurs 
        """
        return False
    
    def loadScreen(self, newScreen):
        """
        Queue up the next screen to load. 
        """
        self.nextScreen = newScreen
        
    def getNextScreen(self):
        """
        Returns the screen queued up to load next. The screen is popped off the
        1-level stack, so only call this method once per screen  
        """
        nextScreen = self.nextScreen
        self.nextScreen = None
        return nextScreen