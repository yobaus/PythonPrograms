# based on https://www.reddit.com/r/beginnerprojects/comments/1i8vt5/project_mad_libs_story_maker/
# By Pete Baus 9/15/2019

WordList = []
AAn = []


def Madlibs():
    Print('Welcome to MadLibs')
    WordList.append(input('Please type a adjective: '))
    WordList.append(input('Please type a adjective: '))
    WordList.append(input('Please type a Noun: '))  # have an an\a
    WordList.append(input('Please type a Noun: '))  # have an an\a
    WordList.append(input('Please type a plural Noun: '))
    WordList.append(input('Please type a name of a game: '))
    WordList.append(input('Please type a plural Noun: '))
    WordList.append(input('Please type a plural verb ending  in "ing": '))
    WordList.append(input('Please type a plural verb ending  in "ing": '))
    WordList.append(input('Please type a plural Noun: '))
    WordList.append(input('Please type a plural verb ending  in "ing": '))
    WordList.append(input('Please type a Noun:'))  # have an an\a
    # has a proper noun
    WordList.append((input('Please type a plant:')).capitalize())
    WordList.append((input('Please type a part of the body: ')).capitalize())
    WordList.append(input('Please type a place: '))
    WordList.append(input('Please type a plural verb ending  in "ing": '))
    WordList.append(input('Please type a adjective: '))
    WordList.append(input('Please type a Number: '))
    WordList.append(input('Please type a plural Noun: '))
    # check the first character to see if it's a vowel to set the a/an
    if not ((WordList[2])[0][0]) in ['a', 'e', 'i', 'o', 'u']:
        AAn.append('a')
    else:
        AAn.append('an')
    if not ((WordList[3])[0][0]) in ['a', 'e', 'i', 'o', 'u']:
        AAn.append('a')
    else:
        AAn.append('an')
    if not ((WordList[11])[0][0]) in ['a', 'e', 'i', 'o', 'u']:
        AAn.append('a')
    else:
        AAn.append('an')
    print('\n\nA vacation is when you take a trip to some',
          WordList[0], 'place with your', WordList[1], 'family.')
    print('Usually you go to some place that is near',
          AAn[0], WordList[2], 'or up', AAn[1], WordList[3], '.')
    print('A good vacation place is one where you can ride',
          WordList[4], 'or play', WordList[5], 'or go hunting for', WordList[6], '.')
    print('I like to spend my time', WordList[7], '. or', WordList[8], '.')
    print('When parents go on vacation, they spend their time eating three',
          WordList[9], 'a day, and fathers play golf, and mothers sit around', WordList[10], '.')
    print('Last summer, my little brother fell in',
          AAn[2], WordList[11], 'and get poison', WordList[12], 'all over his', WordList[13], '.')
    print('My family is going to go to the', WordList[14], '.')
    print('Parents need vacatisons more than kids because parents are alaways very \n',
          WordList[15], 'and because they have to work', WordList[16], 'to work', WordList[17])
    print('hours every day all year making enough',
          WordList[18], 'to pay for the vacation.\n\n')


if __name__ == "__main__":
    Madlibs()
