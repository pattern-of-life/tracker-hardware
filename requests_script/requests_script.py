# -*- coding: utf-8 -*-
"""File implements the sending of GPS data from a python REPL.

Accepts up to 2 arguments, or runs with defaults BOX_DATA and DESTINATION.
Refer to the formats of those constants for the format if you want to
supply your own arguments.
"""
from __future__ import unicode_literals
import requests
import sys

UUID = '18fb4590-c931-47d2-a168-0ca5dcd244e5'

# BOX_DATA = [
#     {'time': '10/11/2016 12:01:01', 'lat': '47.619008', 'lng': '-122.351635', 'elevation': '3', 'uuid': 'taco'},
#     {'time': '10/11/2016 12:03:01', 'lat': '47.719008', 'lng': '-123.351635', 'elevation': '4', 'uuid': 'taco'},
#     {'time': '10/11/2016 12:05:01', 'lat': '47.719008', 'lng': '-122.351635', 'elevation': '5', 'uuid': 'taco'},
#     {'time': '10/11/2016 12:07:01', 'lat': '47.619008', 'lng': '-123.351635', 'elevation': '6', 'uuid': 'taco'},
# ]

BOX_DATA = [
    {'time': '10/11/2016 12:01:01', 'lat': '47.618675', 'lng': '-122.351465', 'elevation': '36.000', 'uuid': 'taco'},
    {'time': '10/11/2016 13:01:01', 'lat': '47.628732', 'lng': '-122.361485', 'elevation': '36.400', 'uuid': 'taco'},
    {'time': '10/11/2016 14:01:01', 'lat': '47.638758', 'lng': '-122.371520', 'elevation': '34.800', 'uuid': 'taco'},
    {'time': '10/11/2016 15:01:01', 'lat': '47.648803', 'lng': '-122.381525', 'elevation': '34.600', 'uuid': 'taco'},
    {'time': '10/11/2016 16:01:01', 'lat': '47.658753', 'lng': '-122.391550', 'elevation': '30.600', 'uuid': 'taco'},
    {'time': '10/11/2016 17:01:01', 'lat': '47.668768', 'lng': '-122.401567', 'elevation': '28.500', 'uuid': 'taco'},
    {'time': '10/11/2016 18:01:01', 'lat': '47.678717', 'lng': '-122.411573', 'elevation': '26.000', 'uuid': 'taco'},
    {'time': '10/11/2016 19:01:01', 'lat': '47.688727', 'lng': '-122.421588', 'elevation': '26.200', 'uuid': 'taco'},
    {'time': '10/11/2016 20:01:01', 'lat': '47.698617', 'lng': '-122.431590', 'elevation': '25.600', 'uuid': 'taco'},
    {'time': '10/11/2016 21:01:01', 'lat': '47.708788', 'lng': '-122.441453', 'elevation': '25.000', 'uuid': 'taco'},
    {'time': '10/11/2016 22:01:01', 'lat': '47.718637', 'lng': '-122.451563', 'elevation': '29.200', 'uuid': 'taco'},
    {'time': '10/11/2016 23:01:01', 'lat': '47.728503', 'lng': '-122.461598', 'elevation': '31.200', 'uuid': 'taco'},
    {'time': '10/12/2016 00:01:01', 'lat': '47.738550', 'lng': '-122.471605', 'elevation': '30.800', 'uuid': 'taco'},
    {'time': '10/12/2016 01:01:01', 'lat': '47.748643', 'lng': '-122.481562', 'elevation': '27.100', 'uuid': 'taco'},
    {'time': '10/12/2016 02:01:01', 'lat': '47.758700', 'lng': '-122.491575', 'elevation': '19.900', 'uuid': 'taco'},
    {'time': '10/12/2016 03:01:01', 'lat': '47.768750', 'lng': '-122.501552', 'elevation': '16.400', 'uuid': 'taco'},
    {'time': '10/12/2016 04:01:01', 'lat': '47.778753', 'lng': '-122.511577', 'elevation': '15.800', 'uuid': 'taco'},
    {'time': '10/12/2016 05:01:01', 'lat': '47.788917', 'lng': '-122.521520', 'elevation': '19.500', 'uuid': 'taco'},
    {'time': '10/12/2016 06:01:01', 'lat': '47.798787', 'lng': '-122.531545', 'elevation': '19.200', 'uuid': 'taco'},
]

# DESTINATION = 'http://localhost:8000/device/data/create'
DESTINATION = 'http://www.trackerpy.com/device/data/create'


def send_data_point(data, destination):
    """sends individual data points to our api."""
    response = requests.post(destination, data=data)
    print('Request sent, status code:', response.status_code)
    print(response.content)


if __name__ == '__main__':
    """Sends the test_data to the destination.  Accepts up to 2 arguments."""
    destination = None
    test_data = None
    uuid = None
    print("Script is running with the following arguments: ", sys.argv)
    if len(sys.argv) > 4:
        raise TypeError("Too many arguments, we only accept three.")
    elif len(sys.argv) == 4:
        uuid = sys.argv[1]
        destination = sys.argv[2]
        test_data = sys.argv[3]
    elif len(sys.argv) == 3:
        uuid = sys.argv[1]
        destination = sys.argv[2]
    elif len(sys.argv) == 2:
        uuid = sys.argv[1]
    if uuid is None:
        uuid = UUID
    if destination is None:
        destination = DESTINATION
    if test_data is None:
        test_data = BOX_DATA
    for point in test_data:
        point['uuid'] = uuid
        send_data_point(point, destination)
    print('All data sent.')
