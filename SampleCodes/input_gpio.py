import Adafruit_BBIO.GPIO as GPIO
 
GPIO.setup("P9_14", GPIO.IN)
 
while True:
    if GPIO.input("P9_14"):
        print("HIGH")
    else:
        print("LOW")
