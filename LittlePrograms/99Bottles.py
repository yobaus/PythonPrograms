# based on https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/
# By Pete Baus 9/10/2019

Number = 99


def bottles():

    # reversed will revers the numbers in the Number range
    for Bottle in reversed((range(Number))):
        if Bottle > 1:
            print(f'{Bottle} bottles of beer on the wall, '
                  f'{Bottle} bottles of beer. Take one down and pass it around, '
                  f'{(Bottle - 1)} bottles of beer on the wall. \n'
                  )
        elif Bottle > 0:
            print(f'{Bottle} bottle of beer on the wall, '
                  f'{Bottle} bottle of beer. Take one down and pass it around, '
                  'no more bottles of beer on the wall. \n'
                  )
        else:
            print('No more bottles of beer on the wall, no more bottles of beer.'
                  ' Go to the store and buy some more, 99 bottles of beer on the wall. \n'
                  )


if __name__ == "__main__":
    bottles()
