# based on https://www.reddit.com/r/beginnerprojects/comments/1j50e7/project_dice_rolling_simulator/
# By Pete Baus 9/25/2019

import random


def DiceRoll():
    Looping = True
    while Looping:
        Sides = (int(input('How many Sides are in the dice?: ')))+1
        Rolls = (int(input('How many times should the dice roll?: ')))
        if Sides == 1 or Rolls == 0:
            print('Please do not leave any lines blank!')
        else:
            Looping = False
    RollList = []

    for number in range(0, Rolls):
        if Sides <= 2:
            # a two side object is a coin and need a zero
            RollList.append(random.randrange(0, Sides))
        else:
            # most dice don't habe a zero
            RollList.append(random.randrange(1, Sides))
    print('Your Rolls are\n', RollList, end='\n\n')
    ListRollCount = {}
    for Roll in set(RollList):
        ListRollCount.update({Roll: str(round(
            RollList.count(Roll) / len(RollList), 4))})
    print('Your Rolls percentage are:')
    printlist(ListRollCount)


def printlist(x):  # Just to make list look better
    for Key in x:
        print("{}: {} %".format(Key, x.get(Key)))


if __name__ == "__main__":
    Loop = True
    while Loop:
        DiceRoll()
