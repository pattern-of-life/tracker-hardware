from GSM import setup_serial, send_command, parse_response, close_serial
from time import sleep

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    commands.append(b'AT')
    commands.append(b'AT+CBC')
    commands.append(b'AT+CGNSPWR?')
    commands.append(b'AT+CGNSSEQ?')
    commands.append(b'AT+CGNSSEQ=?')
    commands.append(b'AT+CGNSSEQ=GGA')
    commands.append(b'AT+CGNSINF')



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
