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
    print('Bytes sent: {}'.format(ser.write(b'AT+CBC\n')))
    time.sleep(0.2)
    bytes_read = 0
    while True:
        data = ser.readline()
        bytes_read += 1
        response += data
        time.sleep(0.1)
        if data == '':
            break
    else:
        print('serial connection was not open')
    print(response)

ser.close()

""" Eventually, you'll want to clean up, but leave this commented for now,
as it doesn't work yet
UART.cleanup()
"""
