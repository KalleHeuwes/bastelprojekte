#Quelle: https://ozeki.hu/p_3054-how-to-setup-a-rotary-encoder-on-raspberry-pi.html
import RPi.GPIO as GPIO
from time import sleep

counter = 1

Enc_A = 17  
Enc_B = 18  
Enc_S = 27

def init():
    print ('Rotary Encoder Test Program')
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.setup(Enc_S, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)
    GPIO.add_event_detect(Enc_S, GPIO.BOTH, callback=switch_decode_short, bouncetime=10)
    return


def rotation_decode(Enc_A):
    global counter
    sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)

    if (Switch_A == 1) and (Switch_B == 0):
        counter += 1
        print ('direction -> ', counter)
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return

    elif (Switch_A == 1) and (Switch_B == 1):
        counter -= 1
        print ('direction <- ', counter)
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else:
        return

def switch_decode_short(Enc_S):
    
    sleep(0.002)
    Switch_S = GPIO.input(Enc_S)
    #print ('Button -> ', Switch_S)

    if (Switch_S == 0):
        print ('Button up')
        
    if (Switch_S == 1):
        print ('Button down')

    return

def switch_decode(Enc_S):
    
    sleep(0.002)
    Switch_S = GPIO.input(Enc_S)
    #print ('Button -> ', Switch_S)

    if (Switch_S == 1):
        print ('Button down')
        while Switch_S == 1:
            Switch_S = GPIO.input(Enc_S)
        return
    elif (Switch_S == 0):
        print ('Button up')
        while Switch_S == 0:
            Switch_S = GPIO.input(Enc_S)
        return

    else:
        return
    
def main():
    try:
        init()
        while True :
            sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()