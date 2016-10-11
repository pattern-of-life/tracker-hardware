import Adafruit_BBIO.UART as UART
import serial
import time

# UART.setup("UART2")


def serial_setup():
    """opens a serial connection and returns it"""
    ser = serial.Serial(port="/dev/ttyO2", baudrate=9600, timeout=2)
    ser.close()
    time.sleep(0.1)
    ser.open()
    time.sleep(0.1)
    return ser


def serial_close(ser):
    """close serial connection"""
    ser.close()


def send_command(ser, com):
    """send a AT command and return the response"""
    response = ''
    data = ''

    if ser.isOpen():
        print('Bytes sent: {}'.format(ser.write(com)))
        print(ser.write(com))
        bytes_read = 0
        while True:
            data = ser.readline()
            bytes_read += 1
            response += data
            if data == '':
                break
    else:
        print('serial connection was not open')
    return response


ser = serial_setup()

print(send_command(ser, b'AT'))
print(send_command(ser, b'AT'))
print(send_command(ser, b'AT'))
print(send_command(ser, b'AT+SAPBR=3,1,"Contype","GPRS"'))
print(send_command(ser, b'AT+SAPBR=3,1,"APN","www"'))
print(send_command(ser, b'AT+SAPBR=1,1'))
print(send_command(ser, b'AT+SAPBR=2,1'))
