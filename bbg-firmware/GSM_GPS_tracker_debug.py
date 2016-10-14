from serial import Serial
from time import sleep
from GSM_debug import setup_serial, send_command, close_serial
from GSM_debug import handle_commands, gps_setup, gps_get_data, gps_get_point
from GSM_debug import gps_format_datetime
import os


def www_open_connection():
    """ Send the commands to the GSM module to open a WWW connection """
    commands = []
    commands.append('AT')
    commands.append('AT+SAPBR=3,1,"Contype","GPRS"')
    commands.append('AT+SAPBR=3,1,"APN","www"')
    commands.append('AT+SAPBR=1,1')
    commands.append('AT+SAPBR=2,1')
    commands.append('AT+SAPBR=2,1')
    return commands


def www_close_connection():
    """close the www connection"""
    commands = ['AT+SAPBR=0,1']
    commands.append('AT+SAPBR=2,1')
    return commands


def http_send_post(url, payload):
    """ Send an HTTP POST request to REST endpoint"""
    commands = []
    length = len(payload)

    commands.append('AT+HTTPINIT')
    commands.append('AT+HTTPPARA="CID",1')
    commands.append('AT+HTTPPARA="URL","{}"'.format(url))
    commands.append('AT+HTTPPARA="CONTENT","application/x-www-form-urlencoded"')
    commands.append('AT+HTTPDATA={},10000'.format(length))
    commands.append(payload)
    commands.append('AT+HTTPACTION=1')
    commands.append('AT+HTTPTERM')
    return commands


if __name__ == "__main__":

    log_path = '/media/card/tracker/'
    file_name = 'tracker_log.csv'
    debug_log = 'tracker_debug.txt'
    LOG_FILE = os.path.join(log_path, debug_log)
    file_path = os.path.join(log_path, file_name)
    fff = open(file_path, 'a')
    fff.write("count, uuid, time, lat, lng, elevation\n")
    fff.close()
    ser = setup_serial()
    uuid = '107639e9-043f-42a5-826d-32cc920667ae'

    handle_commands(ser, gps_setup())
    handle_commands(ser, www_open_connection())

    count = 3600
    for i in range(count):

        word, bytes_sent = handle_commands(ser, gps_get_point())
        time, lat, lng, el, valid_gps = gps_get_data(word)
        if valid_gps:

            time = gps_format_datetime(time)
            url = 'http://ec2-54-191-114-88.us-west-2.compute.amazonaws.com/device/data/create'
            payload = 'uuid={}&time={}&lat={}&lng={}&elevation={}'.format(uuid, time, lat, lng, el)
            print('\n\nPayload: {}'.format(payload))
            print('Count: {}\n\n'.format(count))
            handle_commands(ser, http_send_post(url, payload))
            print("Logging dat to file")
            fff = open(file_path, 'a')
            fff.write("{},{},{},{},{},{}\n".format(i, uuid, time, lat, lng, el))
            fff.close()
        else:
            print("\nNo GPS count: {}\n".format(i))
        sleep(1)

    handle_commands(ser, www_close_connection())
    close_serial(ser)
