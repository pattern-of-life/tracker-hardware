""" This is my library file """
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


def parse_gps(word):
    """ parse the CGNSINF response
    ('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)
    """
    split_word = word.split(':')
    split_word = split_word[1].split('\r\n')
    split_word = split_word[0].split(',', )
    sw = split_word
    # print("Datetime: {} Lat: {} Lng: {} Alt: {} Speed: {} Course: {}"
    #       .format(sw[2], sw[3], sw[4], sw[5], sw[6], sw[7]))
    return split_word


def read_gps_datetime(datetime_str):
    year = datetime_str[:4]
    month = datetime_str[4:6]
    day = datetime_str[6:8]
    hours = datetime_str[8:10]
    minutes = datetime_str[10:12]
    seconds = datetime_str[12:14]
    return '{}/{}/{} {}:{}:{}'.format(
        year, month, day, hours, minutes, seconds
    )


def get_gps_data():
    """ Get data from the GPS """
    


def handle_commands(ser, commands):
    for com in commands:
        response = send_command(ser, com)
        # print(response)

        count = 1
        while count:
            if com == b'AT+HTTPREAD':
                print("Last command was: AT+HTTPREAD")
                sleep(3)
                response = send_command(ser, b'AT+HTTPREAD')
                print('Index of ACTION: {}'.format(response[0].find('ACTION:')))
                # print(response)
                count -= 1

            else:
                break

        for i in response:
            if type(i) == str and 'ERROR' in i:
                sleep(1)
                print("Resending command: {}".format(com))
                response = send_command(ser, com)

    print(response)
    return response
