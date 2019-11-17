# based on https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/
# By Pete Baus 11/7/2019
import urllib.request
import json
import time


class Reddit():
    def __init__(self):
        self.old = False  # just set to false to have them made
        self.Title = False
        self.Reload()

    def Reload(self):
        loop = True
        self.old = self.Title
        while loop:
            loop = False
            try:
                self.html = urllib.request.urlopen(
                    'http://www.reddit.com/r/todayilearned/new/.json')
            except urllib.error.HTTPError as err:
                if err.code == 404:
                    print('Site unavable')
                    time.sleep(30)
                    loop = True
                if err.code == 429:
                    print('Could not connected tying, again in 30 seconds.')
                    time.sleep(30)
                    loop = True
        json_obj = (json.load(self.html))
        self.Title = (json_obj['data']['children'][0]['data']['title'])
        self.Author = (json_obj['data']['children']
                       [0]['data']['author_fullname'])
        self.PermaLink = 'www.reddit.com' + (json_obj['data']['children']
                                             [0]['data']['permalink'])
        self.Format()

    def Format(self):
        new = (self.Title .split(' '))
        if 'TIL' in new:
            new.remove('TIL')
        if 'TIL:' in new:
            new.remove('TIL:')
        if 'That' in new:
            new.remove('That')
        elif 'that' in new:
            new.remove('that')
        new = ' '.join(new)  # compinds the list new in to a single string
        new = new.capitalize()
        if not new[(len(new)-1)] == '.':  # add a period to the end of the fact!
            new = new + '.'
        self.Title = new


def run():
    log = True if input(
        'Do you want a log file? y/n: ') in ['y', 'Y', 'Yes', 'yes'] else False
    if log:
        from pathlib import Path
        from datetime import date
        LocalPath = Path(f"./{(date.today())}.txt")
        print(f"Path to file {LocalPath}")
    loop = True
    TIL = Reddit()
    while loop:
        if not TIL.old == TIL.Title:  # check to see if it the same fact!
            fact = f"'{TIL.Title}', By {TIL.Author} \n{TIL.PermaLink}\n"
            if log:
                file = open(LocalPath, 'a+')
                file.write(fact)
                file.close()
            print(fact)
        time.sleep(30)
        TIL.Reload()


if __name__ == "__main__":
    run()
