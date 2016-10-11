from serial import Serial
from time import sleep


def setup_serial():
    """ Setup serial connection """
    ser = Serial(port="/dev/ttyO2", baudrate=9600, timeout=0)
    ser.close()
    sleep(0.1)
    ser.open()
    sleep(0.1)

    return ser
    # if ser.isOpen():
    #     return True
    # else:
    #     return False


def send_command(ser, com):
    """ Send a Command to the SIM808 module
        Returns response and the # bytes_sent """
    data = ''
    response = ''

    if ser.isOpen():
        bytes_sent = ser.write(com + b'\n')
        sleep(0.1)
        while True:
            data = ser.readline()
            sleep(0.1)
            if data == '':
                break
            response += data
        return response, bytes_sent


def close_serial(ser):
    ser.close()

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    commands.append(b'AT')
    commands.append(b'AT+CBC')
    commands.append(b'AT+SAPBR=3,1,"Contype","GPRS"')
    commands.append(b'AT+SAPBR=3,1,"APN","www"')
    commands.append(b'AT+SAPBR=1,1')
    commands.append(b'AT+SAPBR=2,1')
    commands.append(b'AT+HTTPINIT')
    commands.append(b'AT+HTTPPARA="URL","http://ec2-52-33-25-11.us-west-2.compute.amazonaws.com/"')
    commands.append(b'AT+HTTPACTION=0')
    commands.append(b'AT+HTTPREAD')
    commands.append(b'AT+HTTPREAD')

    for com in commands:
        response = send_command(ser, com)
        print(response)
        if 'ERROR' in response:
            response = send_command(ser, com)
            print(response)
    # print(send_command(ser, b'AT+CBC'))
    # print(send_command(ser, ''))
    close_serial(ser)
