# based on https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/
# By Pete Baus 9/17/2019
# Note Floating point numbers would have make this harder, so I just made it one big number. works better with change!


def ChangeMaker():
    ChangDeict = {}
    TotalPrice = input('\nPlease type the total price owed: ')
    GivenMoney = input('Please type the total money given: ')

    # if they input a number without a decimal it will add .00 to the end
    GivenMoney = (GivenMoney + '.00') if not '.' in GivenMoney else GivenMoney
    TotalPrice = (TotalPrice + '.00') if not '.' in TotalPrice else TotalPrice

    Change = ((int(GivenMoney.replace(".", ""))) -
              (int(TotalPrice.replace(".", ""))))

    ChangDeict.update({'TwentyDollar': (Change // 2000)})
    Change = Change % 2000
    ChangDeict.update({'TenDollars': (Change // 1000)})
    Change = Change % 1000
    ChangDeict.update({'Dollar': (Change // 100)})
    Change = Change % 100
    ChangDeict.update({'Quarter': (Change // 25)})
    Change = Change % 25
    ChangDeict.update({'Dime': (Change // 10)})
    Change = Change % 10
    ChangDeict.update({'Nickel': (Change // 5)})
    Change = Change % 5
    ChangDeict.update({'Penny': (Change // 1)})
    Change = Change % 1

    print('\nThe change due is ')
    for Coin in ChangDeict:
        if ChangDeict[Coin]:
            print(ChangDeict[Coin], Coin)


def Caller():
    K = True
    while K:
        ChangeMaker()


if __name__ == "__main__":
    Caller()
