from serial import Serial
from time import sleep
from GSM import setup_serial, send_command, close_serial
from GSM import handle_commands


def open_www_connection(ser):
    """ Send the commands to the GSM module to open a WWW connection """
    commands = []

    commands.append('AT')
    commands.append('AT+SAPBR=3,1,"Contype","GPRS"')
    commands.append('AT+SAPBR=3,1,"APN","www"')
    commands.append('AT+SAPBR=1,1')
    commands.append('AT+SAPBR=2,1')

    handle_commands(ser, commands)


def close_www_connection(ser):
    """close the www connection"""
    commands = ['AT+SAPBR=0,1']
    handle_commands(ser, commands)


def send_http_post(ser, url, payload):
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

    handle_commands(ser, commands)


if __name__ == "__main__":

    ser = setup_serial()
    uuid = '107639e9-043f-42a5-826d-32cc920667ae'
    time, lat, lng, el = get_gps_data()

    url = 'http://ec2-52-35-206-130.us-west-2.compute.amazonaws.com/device/data/create/'
    payload = 'uuid={}&time={}&lat={}&lng={}&elevation={}'.format(uuid, time, lat, lng, el)

    setup_serial()
    open_www_connection(ser)
    send_http_post(ser, url, payload)
    close_serial(ser)
