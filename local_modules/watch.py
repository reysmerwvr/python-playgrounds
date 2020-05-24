import os
import time
import datetime

while True:
    os.system('clear')
    date_time = datetime.datetime.now()
    print("{}:{}:{}".format(date_time.hour, date_time.minute, date_time.second))
    time.sleep(1)
