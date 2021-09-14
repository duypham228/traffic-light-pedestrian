
from time import sleep
import sys
import RPi.GPIO as GPIO
from gpiozero import LED, Button
from signal import pause

display_list = [20,21,26,19,13,16,12]

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

for pin in display_list:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

#button
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(True)

#light #2
green_2 = LED(22)
red_2 = LED(27)
blue_2 = LED(17)

#light #1
green_1 = LED(23)
red_1 = LED(18)
blue_1 = LED(24)



# DIGIT map as array of array
arrSeg = [[1,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [1,1,0,1,1,0,1],
          [1,1,1,1,0,0,1],
          [0,1,1,0,0,1,1],
          [1,0,1,1,0,1,1],
          [1,0,1,1,1,1,1],
          [1,1,1,0,0,0,0],
          [1,1,1,1,1,1,1],
          [1,1,1,1,0,1,1]]

GPIO.output(6,0) # DOT pin


def countDown():
    for count in range (10):
      GPIO.output(display_list, arrSeg[9-count])
      if count == 9:
          red_1.on()
          red_2.off()
          green_2.on()
      if count == 5:
          green_1.off()
          blue_1.blink(0.5,0.5,4)
      sleep(1)
      
      isCountDone = True

def greenToBlue():
    green_2.off()
    red_2.off()
    blue_2.blink(0.5,0.5,3)
  
while True:
    #if not isIn20: 
    green_2.on()
    button.wait_for_press()
    green_2.off()
    
    if GPIO.input(25) == GPIO.HIGH:
        greenToBlue()
        sleep(3)
        red_2.on()
        red_1.off()
        green_1.on()
        countDown()
        sleep(7)

