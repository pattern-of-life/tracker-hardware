from GSM import setup_serial, send_command, parse_response, close_serial
from time import sleep
from GSM import handle_commands

if __name__ == "__main__":

    ser = setup_serial()
    commands = []
    # commands.append(b'AT+CGPSPWR=0')
    # commands.append('AT+CGPSINF=0')
    # commands.append('AT+CGNSPWR=0')
    # commands.append('AT+CGNSURC=0')
    commands.append('AT+CGNSTST=0')   # stop sending raw CGNS data to uart
    handle_commands(ser, commands)

    close_serial(ser)
