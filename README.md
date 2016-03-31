# RaspberryPi LCARS Interface

Star Trek [LCARS](https://en.wikipedia.org/wiki/LCARS) interface for [Raspberry Pi](https://raspberrypi.org/) using [Pygame](http://www.pygame.org). 

The code is an example of implementing a custom MovieOS-style interface for your RaspberryPi projects that include the RaspberryPi touch screen (e.g. home automation control panel). The LCARS assets can be replaced with assets from any other style of user interface (e.g. from games, cartoons, or TV series).

[![screenshot 1](screenshot.png)](https://youtu.be/HCEL9O3ie40)

(Click screenshot for a video)

# Global Config

- [UI_PLACEMENT_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L7) - if set to ```True```, allows you to long-press any widget (except background items) and then drag them to any location. When you release the widget, it's new top and left co-ordinates are printed in the console, which you can use in your code to place the widget there.
- [DEV_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L10) - if set to ```True```, will show the mouse cursor, for example. The mouse cursor is useful during development (on a non-touch screen).

# Usage

- The starting point for modifying this interface to your needs is [the initial screen that is loaded](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L26), which is ```ScreenAuthorize```. The screens are defined in the ```screens``` folder.
- Screens extend the ```LcarsScreen``` class and define a ```setup()``` method, and optionally the ```handleEvents()``` and ```update()``` methods.
- The ```setup()``` method initializes the widgets to display. See [lcars_widgets.py](https://github.com/tobykurien/rpi_lcars/blob/master/app/widgets/lcars_widgets.py) for some implemented widgets. Currently, only the ```LcarsButton``` can take a click handler (but it's easy to apply this to other widgets).
- The ```handleEvents()``` method is used to respond to clicks. If this method returns ```True```, the event is "consumed", otherwise other widgets get a chance to act on the event. It is important to call the base class ```handleEvent``` method to give it a chance to handle things like long-press-to-drag, etc.
- The method ```loadScreen()``` can be called to open a new screen. There is no backstack, so you'll have to manage the screen flows manually.

# Notes

- Although not implemented in the demo, an interpolator is provided to allow for animations. To see how this can be used, see the [LcarsMoveToMouse](https://github.com/tobykurien/rpi_lcars/blob/master/app/widgets/sprite.py#L67-L89) widget, which smoothly follows screen touches/mouse clicks.
- The [applyColour()](https://github.com/tobykurien/rpi_lcars/blob/master/app/widgets/sprite.py#L59-L65) method is used to take an image asset of a uniform colour (e.g. white) and change it's colour to any other colour. This is how buttons of various colours are created from one asset. However, currently this is a very simple implementation which results in aliasing artifacts, which is why the buttons look aliased. The advantage of this method is that it is trivial to use it to add highlighting of touches on buttons and keep the number of assets required to a minimum.

# Credits

- LCARS graphical user interface is copyright [CBS Studios Inc.](http://www.cbs.com/) and is subject to [the fair use statute](http://www.lcars.mobi/legal/)
- LCARS images and audio assets from [lcarscom.net](http://www.lcarscom.net)
- Sample weather image from the [SABC](http://www.sabc.co.za)


