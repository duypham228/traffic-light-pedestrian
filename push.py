import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def hey(channel):
    print("HEY")
    
GPIO.add_event_detect(25, GPIO.RISING, callback=hey)


GPIO.cleanup()