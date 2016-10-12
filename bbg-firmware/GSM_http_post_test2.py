from serial import Serial
from time import sleep
from GSM import setup_serial, send_command, close_serial
from GSM import handle_commands, gps_setup, gps_get_data, gps_get_point
from GSM import gps_format_datetime


def www_open_connection():
    """ Send the commands to the GSM module to open a WWW connection """
    commands = []
    commands.append('AT')
    commands.append('AT+SAPBR=3,1,"Contype","GPRS"')
    commands.append('AT+SAPBR=3,1,"APN","www"')
    commands.append('AT+SAPBR=1,1')
    commands.append('AT+SAPBR=2,1')
    return commands


def www_close_connection():
    """close the www connection"""
    commands = ['AT+SAPBR=0,1']
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
    commands.append('AT+HTTPTERM')
    return commands


if __name__ == "__main__":

    ser = setup_serial()
    uuid = '107639e9-043f-42a5-826d-32cc920667ae'

    handle_commands(ser, gps_setup())
    word, bytes_sent = handle_commands(ser, gps_get_point())
    time, lat, lng, el = gps_get_data(word)
    time = gps_format_datetime(time)
    url = 'http://ec2-52-35-206-130.us-west-2.compute.amazonaws.com/device/data/create/'
    payload = 'uuid={}&time={}&lat={}&lng={}&elevation={}'.format(uuid, time, lat, lng, el)
    print('\n\nPayload: {}\n\n'.format(payload))
    handle_commands(ser, www_open_connection())
    handle_commands(ser, http_send_post(url, payload))
    handle_commands(ser, www_close_connection())
    close_serial(ser)
