# based on https://www.reddit.com/r/beginnerprojects/comments/1bytu5/projectmenu_calculator/
# By Pete Baus 9/23/2019

import time
Food = {
    'None': 0,
    'Chicken Strips': 350,
    'French Fries': 250,
    'Hamburger': 400,
    'Hotdog': 350,
    'Large Drink': 175,
    'Medium Drink': 150,
    'Milk Shake': 225,
    'Salad': 375,
    'Small Drink': 125
}


def MenuCalculator():
    Price = 0
    num = 0
    for Key in Food:

        print("{}. {}, {:.2f}".format(num, Key, Food.get(Key)*.01))
        num += 1
    InputOrder = input('\nWhat the Oder!?: ')
    Oder = list(InputOrder)
    for Nummber in Oder:
        Price += (list(Food.values())[int(Nummber)])
        Key = (list(Food)[int(Nummber)])
        CFood = (list(Food.values())[int(Nummber)])

        print(("{}, {:.2f}".format(Key, CFood*.01)))

    print("\nYour total is: ${:.2f} \n\n".format((Price * .01)))
    time.sleep(5)


if __name__ == "__main__":
    while 1 < 2:
        MenuCalculator()
