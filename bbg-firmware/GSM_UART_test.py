import Adafruit_BBIO.UART as UART
import serial
import time

# UART.setup("UART2")

ser = serial.Serial(port="/dev/ttyO2", baudrate=9600, timeout=0)
ser.close()
time.sleep(0.1)
ser.open()
time.sleep(0.1)

response = ''
data = ''

if ser.isOpen():
    print "Serial is open!"
    print('Bytes sent: {}'.format(ser.write(b'AT')))

    bytes_read = 0
    while True:
        data = ser.readline()
        bytes_read += 1
        response += data
        if data == '':
            break


    print(response)

ser.close()

""" Eventually, you'll want to clean up, but leave this commented for now,
as it doesn't work yet
UART.cleanup()
"""
