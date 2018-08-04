# mycroft-lightbar.mycroftai
Mycroft skill to control a WS8211 LED string

The lightbar consists of 20 RGB LED modules, each commanded by a WS8211 controller chip.  There is a daisy-chain serial bus jumping from one LED to the next to form the chain.  The first LED is connected to a ESP8266 NodeMCU module.  There is a 3V3 / 5V level shifter in between.  The ESP8266 runs an Arduino sketch that commands the LEDs.  There are several modes.

Off.
Fade up to full white.
50% white.
100% white.
50% blue.
100% blue.
50% green.
100% green.
50% red.
100% red.
50% yellow.
100% yellow.
Knight rider chase in red with after glow.
Running random colour changing.

The ESP8266 presents a simple web page via wifi that allow the light modes to be selected via radio buttons and an Action button.

This skill generates the form extension to the web site call, that commands the mode of the light bar.

My light bar is static on 192.168.1.19.

While this repository does not conatain the light bar sketch it does show a working example of writing form data to a web page.  I will endevour to add the sketch as another repository in due course.
