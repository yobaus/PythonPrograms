# based on https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/
# By Pete Baus 11/18/2019
import urllib.request
import json
import time


class Weather:
    def __init__(self, Zip):
        self.ZipCode = Zip
        self.Reload()

    def Reload(self):

        loop = True
        url = f"http://api.openweathermap.org/data/2.5/forecast?zip={self.ZipCode}&appid=85040350cee8a7829ddc4b7aede9f420"
        while loop:
            loop = False
            try:
                self.html = urllib.request.urlopen(
                    url)
            except urllib.error.HTTPError as err:
                if err.code == 404:
                    print('Site unavable')
                    print(url, self.ZipCode)
                    time.sleep(30)
                    loop = True
                if err.code == 429:
                    print('Could not connected tying, again in 30 seconds.')
                    time.sleep(30)
                    loop = True
        json_obj = (json.load(self.html))
        self.City_Name = json_obj['city']['name']

        temp_max = self.NumberFix((json_obj['list'][0]['main']['temp_max']))
        temp_min = self.NumberFix((json_obj['list'][0]['main']['temp_min']))
        temp_date = self.ConvertTime((json_obj['list'][0]['dt_txt']))
        weather_list = []
        self.Forrcast = []

        for part in json_obj['list']:
            if (self.ConvertTime(part['dt_txt'])[2]) == temp_date[2]:
                part_temp_min = self.NumberFix((part['main']['temp_min']))
                part_temp_max = self.NumberFix((part['main']['temp_max']))
                temp_min = part_temp_min if part_temp_min < temp_min else temp_min
                temp_max = part_temp_max if part_temp_max > temp_max else temp_max
                weather_list.append(part['weather'][0]['description'])
            else:
                self.Forrcast.append([temp_date, temp_max, temp_min,
                                      (self.most_frequent(weather_list))])
                temp_date = self.ConvertTime(part['dt_txt'])
                temp_max = self.NumberFix((part['main']['temp_max']))
                temp_min = self.NumberFix((part['main']['temp_min']))
                weather_list = []
        self.Forrcast.append([temp_date, temp_max, temp_min,
                              (self.most_frequent(weather_list))])

    def most_frequent(self, List):
        return max(set(List), key=List.count)

    def ConvertTime(self, T):
        return (time.strptime(T, '%Y-%m-%d %H:%M:%S'))

    def NumberFix(self, temperature):
        temperature = float(temperature)
        return (round((1.8 * (temperature - 273) + 32), 2))


def DayoftheWeek(Number):
    if Number == 0:
        return 'Monday'
    elif Number == 1:
        return'Tuesday'
    elif Number == 2:
        return'Wednesday'
    elif Number == 3:
        return'Thursday'
    elif Number == 4:
        return'Friday'
    elif Number == 5:
        return'Saturday'
    elif Number == 6:
        return'Sunday'


def Month(Number):
    if Number == 1:
        return 'January'
    elif Number == 2:
        return 'February'
    elif Number == 3:
        return 'March'
    elif Number == 4:
        return 'April'
    elif Number == 5:
        return 'May'
    elif Number == 6:
        return 'June'
    elif Number == 7:
        return 'July'
    elif Number == 8:
        return 'August'
    elif Number == 9:
        return 'September'
    elif Number == 10:
        return 'October'
    elif Number == 11:
        return 'November'
    elif Number == 12:
        return 'December'


if __name__ == '__main__':
    Today = Weather((input('What is your zip code?: ')))
    for day in Today.Forrcast:
        print(
            f"On {DayoftheWeek(day[0][6])}, The {day[0][2]} of {Month(day[0][1])} expect {day[3]} with a Hight of {day[1]}F and a low of {day[2]}F \n\n")
