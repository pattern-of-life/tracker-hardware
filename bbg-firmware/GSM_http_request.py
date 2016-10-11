from serial import Serial
from time import sleep


def setup_serial():
    """ Setup serial connection """
    ser = Serial(port="/dev/ttyO2", baudrate=9600, timeout=0)
    ser.close(0)
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
    print(send_command(ser, 'AT+CBC'))
    close_serial(ser)
