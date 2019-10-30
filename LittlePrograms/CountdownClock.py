# based on https://www.reddit.com/r/beginnerprojects/comments/1bvdmq/project_countdown_clock/
# By Pete Baus 10/5/2019

import time


def UserTimeGet():
    Bad = True
    while Bad:
        try:
            UserTime = {}
            UserTime['Year'] = (
                int(input('Please Type the year, Example (2020): ')))
            UserTime['Month'] = ((
                input('Please Type the month, Example (october): ')).title())
            if not UserTime.get('Month'):
                print(
                    '\n\n\nPlease doble check spelling, and do not leave any entry blank!!!')
                time.sleep(3)
                continue
            UserTime['Day'] = (
                int(input('Please Type the day, Example (5): ')))
            UserTime['Hour'] = (
                int(input('Please Type the Hour, Example (14): ')))
            UserTime['Minute'] = (
                int(input('Please Type the minute, Example (15): ')))
            Months = {
                'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9,
                'October': 10,
                'November': 11,
                'December': 12
            }
        except:
            print(
                '\n\n\nDo not leave any entry blank!!!')
            time.sleep(5)
            Bad = True
        else:
            Bad = False
        if UserTime['Month'] in Months.keys():
            UserTime.update({'Month': (Months[(UserTime['Month'])])})
        else:
            print('Please make sure month is spelled correctly!!')
            Bad = True

        if not Bad:
            # Changes the text Month to there number!

            date_time = '{}.{}.{} {}:{}:0'.format(
                UserTime['Day'], UserTime['Month'], UserTime['Year'], UserTime['Hour'], UserTime['Minute'])
            pattern = '%d.%m.%Y %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date_time, pattern)))
            ETime = (time.localtime(epoch))
        Time = time.localtime()
        if Time < ETime:
            return ETime
        else:
            print('That time has passed, please enter a time that has not passed!')
            Bad = True


def CountDown():
    ETime = UserTimeGet()
    SecTime = -1
    EndTime = False
    while not EndTime:
        Time = time.localtime()
        Contdown = [
            ETime.tm_year - Time.tm_year,
            ETime.tm_mon - Time.tm_mon,
            ETime.tm_mday - Time.tm_mday,
            abs(ETime.tm_hour - Time.tm_hour),
            abs(ETime.tm_min - Time.tm_min),
            abs(ETime.tm_sec - Time.tm_sec),
        ]
        if Contdown[5] == 1 and Contdown[5] < 60:  # will displace a extra one min
            Contdown[4] = 0
        elif Contdown[5] < 60 and not Contdown[5] == 0:
            Contdown[4] -= 1

        if Time.tm_sec > SecTime:
            print('\n\n\n\n\n\n\n\n\n\n\n\nThe Curent Time is \n',
                  time.asctime(Time))
            print('You have {} Years, {} Months, {} Days, {} Hour, {} Minutes {} Seconds left.'.format(
                Contdown[0], Contdown[1], Contdown[2], Contdown[3], Contdown[4], abs(Contdown[5] - 60)))
            print('Your timer is set for:', time.asctime(ETime))
        SecTime = Time.tm_sec
        if Time == ETime:
            print('Times Up!')
            EndTime = True


if __name__ == "__main__":
    CountDown()
