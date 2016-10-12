import Adafruit_BBIO.UART as UART
import serial
import time

# UART.setup("UART2")


def send_commands(commands):
    """opens a serial connection and returns it"""
    ser = serial.Serial(port="/dev/ttyO2", baudrate=9600, timeout=0)
    ser.close()
    time.sleep(0.1)
    ser.open()
    time.sleep(0.1)

    for com in commands:
        response = ''
        data = ''

        if ser.isOpen():
            print('Bytes sent: {}'.format(ser.write(com + b'\n')))
            # print(ser.write(com))
            time.sleep(0.2)
            bytes_read = 0
            while True:
                data = ser.readline()
                # response = data
                if data == '':
                    break
                # if com not in data and data != 'OK':  # or data != '\r\t':
                response = data
                print("Response: {}".format(response))
                time.sleep(0.5)

                # print("Response: {}".format(response))
        else:
            print('serial connection was not open')

    ser.close()


commands = []
# commands.append(b'AT')
# commands.append(b'AT')
# commands.append(b'AT+CGNSPWR?')
# commands.append(b'AT+CBC')
# commands.append(b'AT')
# commands.append(b'AT+SAPBR=3,1,"Contype","GPRS"')
# commands.append(b'AT+SAPBR=3,1,"APN","www"')
# commands.append(b'AT+SAPBR=1,1')
commands.append(b'AT+SAPBR=2,1')
commands.append(b'AT+HTTPINIT')
commands.append(b'AT+HTTPPARA="URL","http://ec2-52-33-25-11.us-west-2.compute.amazonaws.com/"')
commands.append(b'AT+HTTPACTION=0')
commands.append(b'AT+HTTPREAD')
commands.append(b'AT+HTTPREAD')
# commands.append(b'')
send_commands(commands)
