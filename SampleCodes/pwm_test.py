import Adafruit_BBIO.PWM as PWM
#PWM.start(channel, duty, freq=2000, polarity=0)
PWM.start("P9_16", 50)
 
#optionally, you can set the frequency as well as the polarity from their defaults:
PWM.start("P9_16", 50, 1000, 1)

PWM.set_duty_cycle("P9_16", 100)
#PWM.set_frequency("P9_16", 10)

while(True):
	pass

PWM.stop("P9_16")
PWM.cleanup()


