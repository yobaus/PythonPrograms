# based on https://www.reddit.com/r/beginnerprojects/comments/1jg2ru/project_random_wikipedia_article/
# By Pete Baus 11/17/2019
import urllib.request
import json
import time


class Wkik():
    def __init__(self):
        self.Reload()

    def Reload(self):
        # for the most part this will just get the ids
        loop = True
        while loop:
            loop = False
            try:
                self.html = urllib.request.urlopen(
                    'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json')
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
        # This will use the ids to get the link and article's title
        for items in json_obj['query']['random']:
            temp_id = str(items['id'])
            loop = True
            while loop:
                loop = False
                try:
                    temp_html = urllib.request.urlopen(
                        f"https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids={temp_id}&inprop=url&format=json")
                except urllib.error.HTTPError as err:
                    if err.code == 404:
                        print('Site unavable')
                        time.sleep(30)
                        loop = True
                    if err.code == 429:
                        print('Could not connected tying, again in 30 seconds.')
                        time.sleep(30)
                        loop = True
            temp_json_obj = (json.load(temp_html))
            q = input(
                f"Would you like the link for '{temp_json_obj['query']['pages'][temp_id]['title']}'? y/n: ")  # check if the user wants the link
            if q in ['y', 'Y', 'Yes', 'yes']:
                print(
                    f"\n{temp_json_obj['query']['pages'][temp_id]['title']}\n{temp_json_obj['query']['pages'][temp_id]['fullurl']}\n")
                # just Make the program pause
                input("Press enter key when you're ready for the next article.: ")


wiki = Wkik()
