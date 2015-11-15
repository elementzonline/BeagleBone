import Adafruit_BBIO.ADC as ADC
 
ADC.setup()


while(1):

    value = ADC.read_raw("P9_40")
    #value = ADC.read("P9_40")
    print value
