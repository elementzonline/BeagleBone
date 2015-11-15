import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")
UART.setup("UART2")

ser1 = serial.Serial(port="/dev/ttyO1", baudrate=9600, timeout=3)
ser2 = serial.Serial(port="/dev/ttyO2", baudrate=9600, timeout=3)


ser1.close()
ser2.close()

ser1.open()
ser2.open()

if ser1.isOpen():
    print "Serial1 is open!"

if ser2.isOpen():
    print "Serial2 is open"


ser1.write("Hello World!")
print 'data send through hello world'

data_rcv = ser2.readline()

print data_rcv

ser1.close()
ser2.close()
