#!/usr/bin/python
# coding=utf-8
import sys
import csv
import datetime
#run with python timezone.py 8.30 pdt eest
# time timezone timezone-of-conversion

def main():

    # check if correct ammount of arguments doesnt work otherwise
    if len(sys.argv) != 4:
            print('Incorrect amount of arguments.')
            sys.exit(1)

    target_time = -99

    # get the time given in UTC
    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        utc_time = get_utc_time(timezones)
        target_time = utc_time

    #get the time difference of the target to UTC
    with open('timezones.csv', newline='') as csvfile:
        timezones = csv.reader(csvfile, delimiter=',')
        split_time = get_target_time_dif(timezones)
        #split utc time zone to hours and minutes in case of time zones with minutes
        time_dif_h = float(split_time[0])
        time_dif_m = 0
        #check if there was a split before trying to get minutes
        if len(split_time) is 2:
            time_dif_m = float(split_time[1])

        #apply timezone time difference
        target_time = target_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)
    
    to_print = sys.argv[1] + ' ' + sys.argv[2].upper() + ' is ' + target_time.strftime('%H.%M') + ' ' + sys.argv[3].upper()

    print(to_print)



def get_utc_time(timezones):
    for row in timezones:
        #check for timezone argument against csv data
        if row[0].lower() == sys.argv[2].lower():
            utc_timezone = row[2]
            utc_time_dif = utc_timezone[3:]
            entered_time = datetime.datetime.strptime(sys.argv[1], '%H.%M')
            #split utc time zone to hours and minutes in case of time zones with minutes
            split_time = utc_time_dif.split('.')
            time_dif_h = 0 - float(split_time[0])
            time_dif_m = 0
            #check if there was a split before trying to get minutes
            if len(split_time) is 2:
                time_dif_m = float(split_time[1])
        
            #apply timezone time difference
            utc_time = entered_time + datetime.timedelta(hours=time_dif_h, minutes=time_dif_m)
            return utc_time
    #if it get's here timezone code was wrong
    print('First timezone not found')
    sys.exit(1)

def get_target_time_dif(timezones):
    #check for timezone argument against csv data
    for row in timezones:
        if row[0].lower() == sys.argv[3].lower():
            utc_timezone = row[2]
            utc_time_dif = utc_timezone[3:]
            split_time = utc_time_dif.split('.')
            return split_time
    #if it get's here timezone code was wrong
    print('Second timezone not found')
    sys.exit(1)


if __name__ == "__main__":
    main()





