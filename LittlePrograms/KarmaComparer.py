# based on https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/
# By Pete Baus 11/7/2019
import urllib.request
import json
import time


class Reddit():
    def __init__(self):
        loop = True
        while loop:
            loop = False
            self.username = input('Please type the Username: ')
            self.url = 'https://www.reddit.com/user/' + self.username + '.json'
            try:
                self.html = urllib.request.urlopen(self.url)
            except urllib.error.HTTPError as err:
                if err.code == 404:
                    print('Name is unavailable')
                    time.sleep(5)
                    loop = True
                if err.code == 429:
                    time.sleep(5)
                    loop = True

        json_obj = (json.load(self.html))
        self.Title = (json_obj['data']['children'][0]['data']['link_title'])
        self.Karma = (json_obj['data']['children'][0]['data']['score'])
        self.DownVotes = (json_obj['data']['children'][0]['data']['downs'])
        self.UpVotes = (json_obj['data']['children'][0]['data']['ups'])

    def __repr__(self):
        return (f"{self.username} most recent post on '{self.Title}', has {self.UpVotes} up votes, and {self.DownVotes} down votes.\nResulting in {self.Karma} Karma")


def Run():
    Account1 = Reddit()
    Account2 = Reddit()
    if Account1.Karma > Account2.Karma:
        print(f"{Account1.username} has more karma.")
        time.sleep(5)
    elif Account2 > Account1:
        print(f"{Account2.username} has more karma.")
        time.sleep(5)
    elif Account1 == Account2:
        print("Both accounts have the same karma.")
        time.sleep(5)
    print(Account1)
    print(Account2)
    time.sleep(5)


if __name__ == "__main__":
    loop = True
    while loop:
        Run()
