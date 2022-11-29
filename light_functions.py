# simple light controller script

import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

sections = {
    1: range(1, 32, 1),
    2: range(32, 64, 1),
    3: range(64, 96, 1),
    4: range(96, 128, 1)
}
green = Color(0, 255, 0)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
purple = Color(187, 41, 187)
white = Color(255, 255, 255)
off = Color(0, 0, 0)

def lights_off(strip):
    colorWipe(strip, off)

def turn_green(strip):
    colorWipe(strip, green)

def turn_purple(strip):
    colorWipe(strip, purple)

def light_section(strip, section, color):
    colorWipe(strip, Color(0,0,0))
    for i in section:
        strip.setPixelColor(i, color)
        strip.show()

def party(strip):
    color1 = red
    color2 = green
    color3 = blue
    color4 = purple
    color5 = white
    j = 0
    try:
        while True:
            for i in range(strip.numPixels()):
                if i <= 20:
                    strip.setPixelColor(i, color1)
                elif i > 20 and i <= 40:
                    strip.setPixelColor(i, color2)
                elif i > 40 and i <= 60:
                    strip.setPixelColor(i, color3)
                elif i > 60 and i <= 80:
                    strip.setPixelColor(i, color4)
                elif i > 80 and i <= 100:
                    strip.setPixelColor(i, color5)
                elif i > 100 and i <= 120:
                    strip.setPixelColor(i, color1)
                else:
                    strip.setPixelColor(i, color2)
            strip.show()
            time.sleep(0.5)
            if j % 2 == 0:
                color1 = blue
                color2 = purple
                color3 = white
                color4 = red
                color5 = green
            else:
                color1 = red
                color2 = green
                color3 = blue
                color4 = purple
                color5 = white
            j += 1
    except KeyboardInterrupt:
        colorWipe(strip, off)


def colorWipe(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        time.sleep(wait_ms/1000.0)
    strip.show()
    
def christ1(strip = 0, rem = 1):

    for i in range(strip.numPixels()):
        if i % 2 == rem:
            strip.setPixelColor(i, red)
        else:
            strip.setPixelColor(i, green)
    strip.show()

def turn_red(strip):
    colorWipe(strip, red)



if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    while True:
        user_in = input("press enter or 0 to quit: ")
        
        if user_in == "0":
            colorWipe(strip, Color(0,0,0), 10)
            quit()
        try:
            while True:
                christ1(strip, 1)
                time.sleep(1)
                christ1(strip, 0)
                time.sleep(1)
        except KeyboardInterrupt:
            colorWipe(strip, Color(0,0,0))