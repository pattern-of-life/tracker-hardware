# import sys
# import io

f = open('log_test.csv', 'w')
f.write("sequence_num,time,altitude,latitude,longitude")

for i in range(100):
    data = '{0},{1},{2},{3},{4}'.format(i, 1000 + 1, 2000 + i, 3000 + i, 4000 + 1)
    f.write(data)

f.close()
