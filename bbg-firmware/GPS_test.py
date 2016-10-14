from GSM import setup_serial, send_command, parse_response, close_serial
from time import sleep


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

    return response


def parse_gps(word):
    """ parse the CGNSINF response
    ('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)
    """
    # word = "('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)"

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

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    commands.append(b'AT')
    commands.append(b'AT+CBC')
    commands.append(b'AT+CGNSPWR?')
    commands.append(b'AT+CGNSPWR=1')
    commands.append(b'AT+CGNSSEQ?')
    commands.append(b'AT+CGNSSEQ=?')
    commands.append(b'AT+CGNSSEQ=GGA')

    handle_commands(ser, commands)

    commands = []
    commands.append(b'AT+CGNSINF')
    count = 1
    while count:
        word, bytes_sent = handle_commands(ser, commands)
        sw = parse_gps(word)
        print("Datetime: {} Lat: {} Lng: {} Alt: {} Speed: {} Course: {}"
              .format(sw[2], sw[3], sw[4], sw[5], sw[6], sw[7]))
        sleep(10)
        count -= 1

    close_serial(ser)
