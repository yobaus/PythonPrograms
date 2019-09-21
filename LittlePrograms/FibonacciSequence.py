# based on https://www.reddit.com/r/beginnerprojects/comments/19r3qg/functionfibonacci_sequence/
# By Pete Baus 9/20/2019
# I Have it print out the whole list, because I think it cool.


def MainInput():
    FibList = [0, 1]
    NumberRange = int(input('How many places?: '))
    if NumberRange <= 2:
        print(FibList[1])
    elif NumberRange == 2:
        print(NumberRange)
    else:
        NumberRange -= 2
    return NumberRange


def FibonacciMaker(NumRange):
    x = 1
    y = 0
    FibList = [0, 1]
    for number in range(0, NumRange):
        z = x
        x = x + y
        y = z
        FibList.append(x)
    return FibList


def FebTest(FibList):
    Test = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
            2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811)
    for Loop in FibList:
        if not Loop in Test:
            print(Loop, 'Bad')


if __name__ == "__main__":
    DoneFebList = FibonacciMaker(MainInput())
    print(DoneFebList)
#    FebTest(DoneFebList)
