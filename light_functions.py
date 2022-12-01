# simple light controller script

import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



#@author Josh gmys
def lowerBrightness():
    if LED_BRIGHTNESS >= 4:
        LED_BRIGHTNESS -= 2


#@author Josh gmys
def increaseBrightNess():
    if LED_BRIGHTNESS <= 20:
        LED_BRIGHTNESS += 2


#@author Josh gmys
def invertColors():
    LED_INVERT = True



sections = {
    1: range(1, 32, 1),
    2: range(32, 64, 1),
    3: range(64, 96, 1),
    4: range(96, 128, 1)
}
#original colors 
green = Color(0, 255, 0)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
purple = Color(187, 41, 187)
white = Color(255, 255, 255)

#new colors

yellow = Color(255,255,0)
skyblue = Color(135,206,235)
orange = Color(255,127,0)
grey = Color(128,128,128)



colorArray = [green,red,blue,purple,white,yellow,skyblue,orange,grey]



off = Color(0, 0, 0)

def skyblue(strip):
    colorWipe(strip,skyblue)

def orange(strip):
    colorWipe(strip,orange)

def yellow(strip):
    colorWipe(strip,yellow)

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

def steelers(strip):
    for i in range(strip.numPixels()):
        if i <= 20:
            strip.setPixelColor(i, grey)
        elif i > 20 and i <= 40:                    
            strip.setPixelColor(i, yellow)
        elif i > 40 and i <= 60:
            strip.setPixelColor(i, white)
        elif i > 60 and i <= 80:
            strip.setPixelColor(i, grey)
        elif i > 80 and i <= 100:
            strip.setPixelColor(i, yellow)
        elif i > 100 and i <= 120:
            strip.setPixelColor(i, white)
        else:
            strip.setPixelColor(i, grey)
    strip.show()

def party(strip):
    color1 = colorArray[0]
    color2 = colorArray[1]
    color3 = colorArray[2]
    color4 = colorArray[3]
    color5 = colorArray[4]
    color6 = colorArray[5]
    color7 = colorArray[6]
    color8 = colorArray[7]
    color9 = colorArray[8]
    color10 = colorArray[0]
    color11 = colorArray[1]
    color12 = colorArray[2]
    color13 = colorArray[3]
    color14 = colorArray[4]
    color15 = colorArray[5]

    j = 0
    try:
        while True:
            for i in range(strip.numPixels()):
                if i <= 10:
                    strip.setPixelColor(i, color1)
                elif i > 10 and i <= 20:
                    strip.setPixelColor(i, color2)
                elif i > 20 and i <= 30:
                    strip.setPixelColor(i, color3)
                elif i > 30 and i <= 40:
                    strip.setPixelColor(i, color4)
                elif i > 40 and i <= 50:
                    strip.setPixelColor(i, color5)
                elif i > 50 and i <= 60:
                    strip.setPixelColor(i, color6)
                elif i > 60 and i <= 70:
                    strip.setPixelColor(i, color7)
                elif i > 70 and i <= 80:
                    strip.setPixelColor(i, color8)
                elif i > 80 and i <= 90:
                    strip.setPixelColor(i, color9)
                elif i > 90 and i <= 100:
                    strip.setPixelColor(i, color10)
                elif i > 100 and i <= 110:
                    strip.setPixelColor(i, color11)
                elif i > 110 and i <= 120:
                    strip.setPixelColor(i, color12)
                elif i > 120 and i <= 130:
                    strip.setPixelColor(i, color13)
                elif i > 130 and i <= 140:
                    strip.setPixelColor(i, color14)
                else:
                    strip.setPixelColor(i, color15)
            strip.show()
            time.sleep(0.5)
            
            if j % 4 == 0:
                color1 = colorArray[1]
                color2 = colorArray[2]
                color3 = colorArray[3]
                color4 = colorArray[4]
                color5 = colorArray[5]
                color6 = colorArray[6]
                color7 = colorArray[7]
                color8 = colorArray[8]
                color9 = colorArray[0]
                color10 = colorArray[1]
                color11 = colorArray[2]
                color12 = colorArray[3]
                color13 = colorArray[4]
                color14 = colorArray[5]
                color15 = colorArray[6]
            elif j % 4 == 1:
                color1 = colorArray[2]
                color2 = colorArray[3]
                color3 = colorArray[4]
                color4 = colorArray[5]
                color5 = colorArray[6]
                color6 = colorArray[7]
                color7 = colorArray[8]
                color8 = colorArray[0]
                color9 = colorArray[1]
                color10 = colorArray[2]
                color11 = colorArray[3]
                color12 = colorArray[4]
                color13 = colorArray[5]
                color14 = colorArray[6]
                color15 = colorArray[7]
            elif j % 4 == 2:
                color1 = colorArray[3]
                color2 = colorArray[4]
                color3 = colorArray[5]
                color4 = colorArray[6]
                color5 = colorArray[7]
                color6 = colorArray[8]
                color7 = colorArray[0]
                color8 = colorArray[1]
                color9 = colorArray[2]
                color10 = colorArray[3]
                color11 = colorArray[4]
                color12 = colorArray[5]
                color13 = colorArray[6]
                color14 = colorArray[7]
                color15 = colorArray[8]
            elif j % 4 == 3:
                color1 = colorArray[0]
                color2 = colorArray[1]
                color3 = colorArray[2]
                color4 = colorArray[3]
                color5 = colorArray[4]
                color6 = colorArray[5]
                color7 = colorArray[6]
                color8 = colorArray[7]
                color9 = colorArray[8]
                color10 = colorArray[0]
                color11 = colorArray[1]
                color12 = colorArray[2]
                color13 = colorArray[3]
                color14 = colorArray[4]
                color15 = colorArray[5]
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