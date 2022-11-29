import speech_recognition as sr

from light_functions import *


func_dict = {"red": turn_red, "green": turn_green, "purple" : turn_purple, "lights off" : lights_off, "Christmas" : christ1}
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        continue


    if command in func_dict:
        func_dict[command](strip)

