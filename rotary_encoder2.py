#Quelle: https://www.elektronik-kompendium.de/sites/raspberry-pi/2703131.htm

###### LÄUFT DAS NUR MIT MicroPython auf dem Pico ????? #####


# Bibliotheken laden
from rotary import Rotary

# Einstellungen
steps = 10
step_max = 60000
step = int(step_max / steps)

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 17
pin_sw = 27

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = int(step_max / 6)

# Funktion
def rotary_changed(change):
    global value
    global step
    global step_max
    if change == Rotary.ROT_CW:
        value = value + step
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - step
        print('Links (', value, ')')
    elif change == Rotary.SW_RELEASE:
        print('Button losgelassen')
    # Korrektur, wenn Ende erreicht
    if value < 0: value = 0
    # Korrektur, wenn Anfang erreicht
    if value >= step_max: value = step_max

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)