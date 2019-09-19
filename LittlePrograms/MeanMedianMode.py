# based on https://www.reddit.com/r/beginnerprojects/comments/1eqt8i/function_mean_median_and_mode/
# By Pete Baus 9/18/2019


def GetNumbers():
    Loop = True
    NumbberList = []
    while Loop:
        k = input('Please Type a number. Type "Done" with Done: ')
        if k in ['Done', 'done', 'D', 'd', '']:
            Loop = False
        elif '.' in k:
            NumbberList.append(float(k))
        else:
            NumbberList.append(int(k))
    return NumbberList


def Mean():
    NumbberList = GetNumbers()
    Avg = 0
    for Number in NumbberList:
        Avg = Avg + Number
    Avg = Avg / len(NumbberList)
    print('That Mean is', Avg)


def Median():
    NumbberList = GetNumbers()
    NumbberList.sort()
    if (len(NumbberList)) % 2:
        print('The median is', NumbberList[(len(NumbberList)) // 2])
    else:
        print('The median is', (NumbberList[(len(NumbberList)) // 2]),
              (NumbberList[(len(NumbberList)) // 2 - 1]))


def Mode():
    ModeList = {}
    ModeFinal = []
    NumbberList = GetNumbers()
    for Number in set(NumbberList):  # makes a list of the repeding numbers
        if NumbberList.count(Number) >= 2:
            ModeList.update({Number: NumbberList.count(Number)})

    for Number in ModeList:
        if ModeList.get(Number) == max(ModeList.values()):
            ModeFinal.append(Number)

    if not ModeFinal:
        print('There is not a Mode')
    else:
        print('The Mode is:', ModeFinal)


if __name__ == "__main__":
    Mean()
    Median()
    Mode()
