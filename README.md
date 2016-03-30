# RaspberryPi LCARS Interface

Star Trek [LCARS](https://en.wikipedia.org/wiki/LCARS) interface for [Raspberry Pi](https://raspberrypi.org/) using [Pygame](http://www.pygame.org). 

The code is an example of implementing a custom MovieOS-style interface for your RaspberryPi projects that include the RaspberryPi touch screen (e.g. home automation control panel). The LCARS assets can be replaced with assets from any other style of user interface (e.g. from games, cartoons, or TV series).

[![screenshot 1](screenshot.png)](https://youtu.be/HCEL9O3ie40)

(Click screenshot for a video)

# Global Config

- [UI_PLACEMENT_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L7) - if set to ```True```, allows you to long-press any widget (except background items) and then drag them to any location. When you release the widget, it's new top and left co-ordinates are printed in the console, which you can use in your code to place the widget there.
- [DEV_MODE](https://github.com/tobykurien/rpi_lcars/blob/master/app/lcars.py#L10) - if set to ```True```, will show the mouse cursor, for example. The mouse cursor is useful during development (on a non-touch screen).

# Credits and Notes

- LCARS graphical user interface is copyright [CBS Studios Inc.](http://www.cbs.com/) and is subject to [the fair use statute](http://www.lcars.mobi/legal/)
- LCARS images and audio assets from [lcarscom.net](http://www.lcarscom.net)
- Sample weather image from the [SABC](http://www.sabc.co.za)


