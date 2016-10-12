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


def parse_response(resp):
    """split the response up by commas"""
    response_list = resp[0].split(',')
    return response_list


def close_serial(ser):
    ser.close()

if __name__ == "__main__":

    ser = setup_serial()
    commands = []

    url = 'http://ec2-52-35-206-130.us-west-2.compute.amazonaws.com/device/data/create/'
    payload = b'UUID=107639e9-043f-42a5-826d-32cc920667ae&dt=20161012165158&lat=47.619055&lng=-122.351692&alt=74.200&bat=98'
    length = len(payload)

    commands.append(b'AT')
    commands.append(b'AT+CBC')
    commands.append(b'AT+SAPBR=3,1,"Contype","GPRS"')
    commands.append(b'AT+SAPBR=3,1,"APN","www"')
    commands.append(b'AT+SAPBR=1,1')
    commands.append(b'AT+SAPBR=2,1')

    commands.append(b'AT+HTTPINIT')
    commands.append(b'AT+HTTPPARA="CID",1')
    commands.append('AT+HTTPPARA="URL","{}"'.format(url))
    commands.append('AT+HTTPPARA="CONTENT","application/x-www-form-urlencoded"')
    commands.append('AT+HTTPDATA={},10000'.format(length))
    commands.append(payload)
    commands.append(b'AT+HTTPTERM')

    for com in commands:
        response = send_command(ser, com)
        print(response)

        count = 1
        while count:
            if com == b'AT+HTTPREAD':
                print("Last command was: AT+HTTPREAD")
                sleep(3)
                response = send_command(ser, b'AT+HTTPREAD')
                print('Index of ACTION: {}'.format(response[0].find('ACTION:')))
                print(response)
                count -= 1

            else:
                break

        for i in response:
            if type(i) == str and 'ERROR' in i:
                sleep(1)
                print("Resending command: {}".format(com))
                response = send_command(ser, com)
                print(response)

    close_serial(ser)
