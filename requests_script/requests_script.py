# -*- coding: utf-8 -*-
"""File implements the sending of GPS data from a python REPL.

Accepts up to 2 arguments, or runs with defaults BOX_DATA and DESTINATION.
Refer to the formats of those constants for the format if you want to
supply your own arguments.
"""
from __future__ import unicode_literals
import requests
import sys
'2016/10/11 12:01:01'
BOX_DATA = [
    {'time': '10/11/2016 12:01:01', 'lat': '47.619008', 'lng': '-122.351635', 'elevation': '3', 'uuid': '18fb4590-c931-47d2-a168-0ca5dcd244e5'},
    {'time': '10/11/2016 12:03:01', 'lat': '47.719008', 'lng': '-123.351635', 'elevation': '4', 'uuid': '18fb4590-c931-47d2-a168-0ca5dcd244e5'},
    {'time': '10/11/2016 12:05:01', 'lat': '47.719008', 'lng': '-122.351635', 'elevation': '5', 'uuid': '18fb4590-c931-47d2-a168-0ca5dcd244e5'},
    {'time': '10/11/2016 12:07:01', 'lat': '47.619008', 'lng': '-123.351635', 'elevation': '6', 'uuid': '18fb4590-c931-47d2-a168-0ca5dcd244e5'},
]

DESTINATION = 'http://localhost:8000/device/data/create'
DESTINATION2 = 'http://ec2-52-33-25-11.us-west-2.compute.amazonaws.com/'


def send_data_point(data, destination):
    """sends individual data points to our api."""
    response = requests.post(destination, data=data)
    import pdb; pdb.set_trace()
    print('Request sent, status code:', response.status_code)
    print(response.content)


if __name__ == '__main__':
    """Sends the test_data to the destination.  Accepts up to 2 arguments."""
    destination = None
    test_data = None
    if len(sys.argv) > 3:
        raise TypeError("Too many arguments, we only accept two.")
    elif len(sys.argv) == 3:
        destination = sys.argv[2]
        test_data = sys.argv[3]
    elif len(sys.argv) == 2:
        destination = sys.argv[2]
    if destination is None:
        destination = DESTINATION
    if test_data is None:
        test_data = BOX_DATA
    for point in test_data:
        send_data_point(point, destination)
    print('All data sent.')
