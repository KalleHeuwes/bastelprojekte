# Quelle: https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-use-a-rotary-encoder-with-the-raspberry-pi
# KY-040
from RPi import GPIO
from time import sleep

clk = 17
dt = 18
sw = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
swLastState = GPIO.input(sw)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                swState = GPIO.input(sw)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print (str(counter) + ', Button: ' + str(swState))
                if swState != swLastState:
                    print('Button: ' + str(swState))
                    sleep(1)
                clkLastState = clkState
                swLastState = swState
                sleep(0.01)
finally:
        GPIO.cleanup()
