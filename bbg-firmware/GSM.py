""" FONA SIM808 library"""
from serial import Serial
from time import sleep


def setup_serial():
    """ Setup serial connection """
    ser = Serial(port="/dev/ttyO2", baudrate=57600, timeout=1)
    ser.close()
    sleep(0.1)
    ser.open()
    sleep(0.1)

    return ser


def parse_response(resp):
    """split the response up by commas"""
    response_list = resp[0].split(',')
    return response_list


def close_serial(ser):
    ser.close()


def gps_get_data(word):
    """Parse the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    sw = word.split(':')
    sw = sw[1].split('\r\n')
    sw = sw[0].split(',', )
    sw[3] = str(sw[3]).replace('.', '%2E')
    sw[4] = str(sw[4]).replace('.', '%2E')
    sw[5] = str(sw[5]).replace('.', '%2E')
    return sw[2], sw[3], sw[4], sw[5]


def gps_parse_raw(word):
    """ parse the CGNSINF response into a list of values
    ('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)
    """
    split_word = word.split(':')
    split_word = split_word[1].split('\r\n')
    split_word = split_word[0].split(',', )
    # sw = split_word
    # print("Datetime: {} Lat: {} Lng: {} Alt: {} Speed: {} Course: {}"
    #       .format(sw[2], sw[3], sw[4], sw[5], sw[6], sw[7]))
    return split_word


def gps_format_datetime(datetime_str):
    """convert CGNS GGA date time into format for REST post"""
    year = datetime_str[:4]
    month = datetime_str[4:6]
    day = datetime_str[6:8]
    hours = datetime_str[8:10]
    minutes = datetime_str[10:12]
    seconds = datetime_str[12:14]
    return '{}%2F{}%2F{}+{}%3A{}%3A{}'.format(
        month, day, year, hours, minutes, seconds
    )


def gps_setup():
    """ Set up the GPS on the SIM808 """
    commands = []
    commands.append('AT')
    commands.append('AT+CBC')
    commands.append('AT+CGNSPWR?')
    commands.append('AT+CGNSPWR=1')
    commands.append('AT+CGNSSEQ?')
    commands.append('AT+CGNSSEQ=?')
    commands.append('AT+CGNSSEQ=GGA')
    return commands


def gps_get_point():
    """ Get a gps data point """
    commands = ['AT+CGNSINF']
    return commands


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

    print('Response: {}'.format(response))
    return response, bytes_sent


def handle_commands(ser, commands):
    for com in commands:
        sleep(.5)
        response = send_command(ser, com)
        # print(response)

        count = 1
        while count:
            if com == 'AT+HTTPREAD':
                print("Last command was: AT+HTTPREAD")
                sleep(3)
                response = send_command(ser, 'AT+HTTPREAD')
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
                # print(response)

    return response
