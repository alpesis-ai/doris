from __future__ import print_function

import time
from upm import pyupm_grove as grove


def main():
    # Create the Grove LED object using GPIO pin 2
    led_red = grove.GroveLed(3)
    led_blue = grove.GroveLed(4)

    # Print the name
    print(led_red.name())
    print(led_blue.name())

    # Turn the LED on and off 10 times, pausing one second
    # between transitions
    for i in range (0,10):
        led_red.on()
        time.sleep(1)
        led_red.off()
        time.sleep(1)

        led_blue.on()
        time.sleep(2)
        led_blue.off()
        time.sleep(2)

    # Delete the Grove LED object
    del led_red
    del led_blue


if __name__ == '__main__':
    main()
