import datetime
import locale
import pytz  # pip3 install pytz


def print_date_time_info(date_time_object):
    print(date_time_object)
    print(date_time_object.year)
    print(date_time_object.month)
    print(date_time_object.day)
    print(date_time_object.hour)
    print(date_time_object.minute)
    print(date_time_object.second)
    print(date_time_object.microsecond)
    print(date_time_object.tzinfo)
    print("{}:{}:{}".format(date_time_object.hour, date_time_object.minute, date_time_object.second))
    print("{}/{}/{}".format(date_time_object.day, date_time_object.month, date_time_object.year))
    print(date_time_object.isoformat())
    print(date_time_object.strftime("%A %d %B %Y %I %M"))
    print("------------------------")


date_time = datetime.datetime.now()
print_date_time_info(date_time)
date_time = datetime.datetime(2000, 1, 1)
print_date_time_info(date_time)
date_time = date_time.replace(year=3000)
print_date_time_info(date_time)
locale.setlocale(locale.LC_ALL, '')
date_time = datetime.datetime.now()
time_to_sum = datetime.timedelta(days=14, hours=4, seconds=1000)
next_time = date_time + time_to_sum
print_date_time_info(next_time)
previous_time = date_time - time_to_sum
print_date_time_info(previous_time)
tokyo_date_time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
print_date_time_info(tokyo_date_time)
print(pytz.all_timezones)
