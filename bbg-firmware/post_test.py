# import requests


# req = requests.get('http://ec2-52-33-25-11.us-west-2.compute.amazonaws.com/')
# print(req)
#
# payload = {'time': "2016123345466", 'lat': '47.619008', 'lng': '-122.351635'}
# r = requests.post('http://ec2-52-33-25-11.us-west-2.compute.amazonaws.com/', data=payload)
# print(r.text)


"""
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

UUID=107639e9-043f-42a5-826d-32cc920667ae&dt=20161012165158&lat=47.619055&lng=-122.351692&alt=74.200&bat=98
"""

AT+HTTPINIT
AT+HTTPPARA="CID",1
AT+HTTPPARA="URL","http://posttestserver.com/post.php"
AT+HTTPPARA="CONTENT","multipart/form-data; boundary=----WebKitFormBoundaryvZ0ZHShNAcBABWFy"
AT+HTTPDATA=192,10000


url = 'http://ec2-52-35-206-130.us-west-2.compute.amazonaws.com/device/data/create/'
payload = b'UUID=107639e9-043f-42a5-826d-32cc920667ae&dt=20161012165158&lat=47.619055&lng=-122.351692&alt=74.200&bat=98'
length = len(payload)

commands.append(b'AT+HTTPINIT')
commands.append(b'AT+HTTPPARA="CID",1')
commands.append('AT+HTTPPARA="URL","{}"'.format(url))
commands.append('AT+HTTPPARA="CONTENT","application/x-www-form-urlencoded"')
commands.append('AT+HTTPDATA={},10000'.format(length))
commands.append(payload)
