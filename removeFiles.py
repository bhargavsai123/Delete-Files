import time
import os
import shutil

path = input('Enter The Path Location: ')
currentTime = time.time()

if os.path.exists(path):
    list = os.listdir(path)
else:
    print('Path Does not Exist')

for file in list:
    file = os.path.join(path, file)
    if os.stat(file).st_ctime < currentTime - 30 * 84600:
        if os.path.isfile(file):
            os.remove(file)
