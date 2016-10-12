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


def parse_battery(word):
    """ parse the CBC battery response
    ('AT+CBC\r\n+CBC: 0,55,3841', 11)
    """
    if '+CBC' in word:
        # word = "('AT+CBC\r\n+CBC: 0,55,3841\r\n', 11)""

        split_word = word.split(':')
        split_word = split_word[1].split('\r\n')
        split_word = split_word[0].split(',', )
        sw = split_word
        print("Battery %: {} Voltage:{}".format(sw[2], sw[3]))

        return split_word

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    commands.append(b'AT')
    commands.append(b'AT+CBC')

    handle_commands(ser, commands)

    commands = []
    commands.append(b'AT+CBC')
    count = 30
    while count:
        word = handle_commands(ser, commands)
        sw = parse_battery(word)
        print("Battery %: {} Voltage:{}".format(sw[2], sw[3]))
        sleep(10)
        count -= 1

    close_serial(ser)
