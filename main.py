import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]
# testing 
leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def numLed(volume):
    numLeds = int(abs(volume * len(leds)))
    return numLeds

pastVol = 0 # initiate previous volume
# main loop
while True:
    volume = microphone.value

    print(volume)
    vol_n = abs(volume -25000)/5000 #normalize microphone value to smaller range
    numLedsOn = numLed(vol_n)

    print(numLedsOn)
    for i, led in enumerate(leds):
        if i < numLedsOn:
            led.value = True  # ON
        else:
            led.value = False  # OFF
    for i in range(numLedsOn):
        if len(leds)-1-i > 0 & len(leds)-1-i <len(leds):
            leds[len(leds)-1-i].value = False
            sleep(0.05)
    
    sleep(0.1)

    # if pastVol < vol_n:
    #     sleep(0.1)

    # else:
    #     sleep(0.25)
    
    # pastVol = vol_n


