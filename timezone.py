#!/usr/bin/python
# coding=utf-8
import sys
import csv
import datetime
#python timezone.py 8.23 pdt eest

def main():
    if len(sys.argv) != 4:
            print('Incorrect amount of arguments.')
            sys.exit(1)

    target_time = -99

    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        utc_time = get_utc_time(timezones)
        target_time = utc_time

    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        split_time = get_target_time_dif(timezones)
        time_dif_h = float(split_time[0])
        time_dif_m = 0
        if len(split_time) is 2:
            time_dif_m = float(split_time[1])

        target_time = target_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)
    
    to_print = sys.argv[1] + ' ' + sys.argv[2].upper() + ' is ' + target_time.strftime('%H.%M') + ' ' + sys.argv[3].upper()

    print(to_print)



def get_utc_time(timezones):
    for row in timezones:
        if row[0].lower() == sys.argv[2].lower():
            utc_timezone = row[2]
            utc_time_dif = utc_timezone[3:]
            entered_time = datetime.datetime.strptime(sys.argv[1], '%H.%M')

            split_time = utc_time_dif.split('.')
            time_dif_h = float(split_time[0])
            time_dif_m = 0
            if len(split_time) is 2:
                time_dif_m = float(split_time[1])
        
            utc_time = entered_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)
            return utc_time

    print('First timezone not found')
    sys.exit(1)

def get_target_time_dif(timezones):
    for row in timezones:
        if row[0].lower() == sys.argv[3].lower():
            utc_timezone = row[2]
            utc_time_dif = utc_timezone[3:]
            split_time = utc_time_dif.split('.')
            return split_time

    print('Second timezone not found')
    sys.exit(1)


if __name__ == "__main__":
    main()





