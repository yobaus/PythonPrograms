# based on https://www.reddit.com/r/beginnerprojects/comments/1idqw1/project_coin_estimator_by_weight/
# By Pete Baus 9/13/2019
Coins = {
    'penny': 2.500,
    'nickel': 5.0,
    'dime': 2.268,
    'quarter': 5.670,
    'halfdollar': 11.340,
    'goldendollar': 8.1,
}


def NumberCheck(x, y):
    if not x:  # if the string is empty it set as 0
        x = 0
    elif any(s in x for s in '.'):  # if it find a decimale if will convert it to a float
        x = (float(x))
    else:
        x = (int(x))
    # if the weight is in pounds it will convert it to grams
    if y in ['pounds', 'Pounds', 'p', 'P']:
        x = (x / 0.0022046)
    return (x)


def StepOne():
    Pounds = input('would you like to use grams or pounds?: ')
    Penny = NumberCheck(input('How much does your penny weigh? '), Pounds)
    Nickel = NumberCheck(input('How much does your nickel weigh? '), Pounds)
    Dime = NumberCheck(input('How much does your dime weigh? '), Pounds)
    Quarter = NumberCheck(input('How much does your quarter weigh? '), Pounds)
    HalfDollar = NumberCheck(
        input('How much does your half dollar weigh? '), Pounds)
    GoldenDollar = NumberCheck(
        input('How much does your Golden Dollar weigh? '), Pounds)

    PennyCount = (round((Penny / (Coins['penny']))))
    PennyWrapper = round(PennyCount / 50)
    NickelCount = (round((Nickel / (Coins['nickel']))))
    NickelWrapper = round(NickelCount / 40)
    DimeCount = (round((Dime / (Coins['dime']))))
    DimeWrapper = round(DimeCount / 50)
    QuarterCount = (round((Quarter / (Coins['quarter']))))
    QuarterWrapper = round(QuarterCount / 40)
    HalfDollarCount = (round((HalfDollar / (Coins['halfdollar']))))
    HalfDollarWrapper = round(HalfDollarCount / 20)
    GoldenDollarCount = (round((GoldenDollar / (Coins['goldendollar']))))
    GoldenDollarWrapper = round(GoldenDollarCount / 25)

    print('\n\nYou have', PennyCount, 'Pennys and you will need',
          PennyWrapper, 'Wrappers!')
    print('You have', NickelCount, 'Nickels and you will need',
          NickelWrapper, 'Wrappers!')
    print('You have', DimeCount, 'Dimes and you will need',
          DimeWrapper, ' Wrappers!')
    print('You have', QuarterCount, 'Quarters and you will need',
          QuarterWrapper, 'Wrappers!')
    print('You have', HalfDollarCount, 'Half Dollar and you will need',
          HalfDollarWrapper, 'Wrappers!')
    print('You have', GoldenDollarCount, 'Half Dollar and you will need',
          GoldenDollarWrapper, 'Wrappers!\n')


def StepTwo():
    print('Welcome to Coin Count!')
    StepOne()
    Rerun = input('would you like to run agin? Y/N: ')
    if Rerun in ['Y', 'y', 'yes', 'Yes']:
        print('\n\n\n\n')
        StepTwo()
    print('\nThank you for using CoinCount!')


if __name__ == "__main__":
    StepTwo()
