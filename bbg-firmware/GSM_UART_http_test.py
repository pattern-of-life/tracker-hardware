import Adafruit_BBIO.UART as UART
import serial
import time

# UART.setup("UART2")


def send_commands(commands):
    """opens a serial connection and returns it"""
    ser = serial.Serial(port="/dev/ttyO2", baudrate=9600, timeout=2)
    ser.close()
    time.sleep(0.1)
    ser.open()
    time.sleep(0.1)

    for com in commands:
        response = ''
        data = ''

        if ser.isOpen():
            print('Bytes sent: {}'.format(ser.write(com)))
            # print(ser.write(com))
            bytes_read = 0
            while True:
                data = ser.readline()
                bytes_read += 1
                response += data
                if data == '':
                    break
            print("Response: {}".format(response))
        else:
            print('serial connection was not open')

    ser.close()


commands = []
commands.append(b'AT')
commands.append(b'AT')
commands.append(b'AT')
commands.append(b'AT+SAPBR=3,1,"Contype","GPRS"')
commands.append(b'AT+SAPBR=3,1,"APN","www"')
commands.append(b'AT+SAPBR=1,1')
commands.append(b'AT+SAPBR=2,1')
send_commands(commands)
