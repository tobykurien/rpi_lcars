# RaspberryPi LCARS Interface

Star Trek [LCARS](https://en.wikipedia.org/wiki/LCARS) interface for [Raspberry Pi](https://raspberrypi.org/) using [Pygame](http://www.pygame.org). 

The code is an example of implementing a custom MovieOS-style interface for your RaspberryPi projects that include the RaspberryPi touch screen (e.g. home automation control panel). The LCARS assets can be replaced with assets from any other style of user interface (e.g. from games, cartoons, or TV series).

[![screenshot 1](screenshot.png)](https://youtu.be/HCEL9O3ie40)

(Click screenshot for a video)

# Global Config

- [UI_PLACEMENT_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L5) - if set to ```True```, allows you to long-press any widget (except background items) and then drag them to any location. When you release the widget, it's new top and left co-ordinates are printed in the console, which you can use in your code to place the widget there.
- [DEV_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L8) - if set to ```True```, will show the mouse cursor, for example. The mouse cursor is useful during development (on a non-touch screen).

# Usage

- The starting point for modifying this interface to your needs is [the initial Screen that is loaded](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L11), which is ```ScreenAuthorize```. The Screens are defined in the ```screens``` folder.
- Screens extend the [```LcarsScreen```](https://github.com/tobykurien/rpi_lcars/blob/master/app/ui/widgets/screen.py) class and define a ```setup()``` method, and optionally the ```handleEvents()``` and ```update()``` methods.
- The ```setup()``` method initializes the widgets to display. See [lcars_widgets.py](https://github.com/tobykurien/rpi_lcars/blob/master/app/ui/widgets/lcars_widgets.py) for some of the implemented widgets. 
- The ```handleEvents()``` method is used to respond to clicks. If this method returns ```True```, the event is "consumed", otherwise other widgets get a chance to act on the event. 
- The ```update()``` method is called once per frame, allowing the Screen to update how it is drawn. Code in here needs to be highly optimized. This method is called *after* the widgets are drawn, but there is a ```pre_update()``` method you can override to draw before the widgets get drawn.
- The method ```loadScreen()``` can be called to open a new Screen. There is no backstack, so you will have to manage the Screen flows manually.

# Installation

- Download or Git clone this repository into a local folder
- Run the ```setup.sh``` script to install the needed dependencies, OR if you have pip, run ```pip install -r requirements.txt```

# Launching

- You can launch the interface from inside an X desktop session by opening a terminal and running ```python lcars.py``` from inside the ```app``` folder.
- To launch the interface from the command line, run the ```run.sh``` script in the project root. Note that you will need to have ```xinit``` installed (```sudo apt-get install xinit```). While you can run it without X, the touch points will be mis-aligned, and so is not feasible.
- You can launch the interface on bootup by adding the following to the ```/etc/rc.local``` file:

```
cd /home/pi/rpi_lcars/app
sudo -u pi xinit /usr/bin/python lcars.py
``` 
The above assumes you want to run the interface from the ```/home/pi/rpi_lcars``` folder as the ```pi``` user. To run as root, simply omit the ```sudo -u pi``` bit.


# Notes

- Although not implemented in the demo, an interpolator is provided to allow for animations. To see how this can be used, see the [LcarsMoveToMouse](https://github.com/tobykurien/rpi_lcars/blob/master/app/ui/widgets/sprite.py#L79-L101) widget, which smoothly follows screen touches/mouse clicks.
- The [applyColour()](https://github.com/tobykurien/rpi_lcars/blob/master/app/ui/widgets/sprite.py#L71-L77) method is used to take an image asset of a uniform colour (e.g. white) and change its colour to any other colour. This is how buttons of various colours are created from one asset. However, currently this is a very simple implementation which results in aliasing artifacts, which is why the buttons look aliased. The advantage of this method is that it is trivial to use it to add highlighting of touches on buttons and keep the number of assets required to a minimum.
- If you are using the [Waveshare 5" or 7" touch screen](https://www.adafruit.com/products/2407) (or similar), then you can use the sample ```boot/config.txt``` to get the screen running at the correct resolution, and install a user-space touch driver, like [this one](https://github.com/derekhe/waveshare-7inch-touchscreen-driver) 

# Credits

- LCARS graphical user interface is copyright [CBS Studios Inc.](http://www.cbs.com/) and is subject to [the fair use statute](http://www.lcars.mobi/legal/)
- LCARS images and audio assets from [lcarscom.net](http://www.lcarscom.net)
- Sample weather image from the [SABC](http://www.sabc.co.za)


