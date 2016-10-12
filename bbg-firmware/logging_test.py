import os

log_path = '/media/card/tracker/'
print('open file')
file_name = 'log_test.csv'
file_path = os.path.join(log_path, file_name)
f = open(file_path, 'w')
print('write header')
f.write("sequence_num,time,altitude,latitude,longitude\n")

print('log data')
for i in range(100):
    data = '{0},{1},{2},{3},{4}\n'.format(i, 1000 + 1, 2000 + i, 3000 + i, 4000 + 1)
    f.write(data)

f.close()
print('close file')
