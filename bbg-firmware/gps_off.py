from GSM import setup_serial, send_command, parse_response, close_serial
from time import sleep
from GSM import handle_commands

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    commands.append(b'AT')
    handle_commands(ser, commands)

    close_serial(ser)
