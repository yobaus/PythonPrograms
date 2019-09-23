# based on https://www.reddit.com/r/beginnerprojects/comments/1irw2j/project_hangman_game/
# By Pete Baus 9/23/2019


import random
from collections import Counter


def HangMan():
    WordList = ('ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule',
                'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra')
    HANGMANPICS = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\ |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\ |
        /   |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\ |
        / \ |
            |
        =========''', '''
                                                            /\  /|
                                                            /  ''  /
                                                            / .o\  ../
                                                            /.'  |\ | '.|
                    __                                    '    |_\|
                    \ \___     .__                             |_|<o>
                    .--""___\..--"/                              |_| |
                .__.|-"""..... ' /                          _____|_|_|\__
        ________\_______________/______________________..-'::::::::::::::::-..___
        ______________________________________________..:::::::::::::::::::::______                          
                    ~       ~           ~        ~                  ~
            ~                     ~                   ~       ~
        ~                 ~                  ~                         ~ ''']

    R = random.randint(0, 64)
    PlayersGuess = []
    Word = (WordList[R])
    WordList = list(Word)
    Loop = True
    WrongCount = 12
    GiveUP = False
    print(Word)
    for n in range(0, (len(Word))):
        PlayersGuess.append('_')
    while Loop == True:
        if WrongCount >= 11:
            print(HANGMANPICS[0])
        elif WrongCount >= 9:
            print(HANGMANPICS[1])
        elif WrongCount >= 7:
            print(HANGMANPICS[2])
        elif WrongCount >= 5:
            print(HANGMANPICS[3])
        elif WrongCount >= 3:
            print(HANGMANPICS[4])
        elif WrongCount >= 1:
            print(HANGMANPICS[5])
        print(PlayersGuess, sep='')
        Guess = (input('What your Guess? or type giveup: ')).lower()
        if Guess == 'giveup':
            print('Awww man, The word was ', Word, '!', sep='')
            break
        if any(Guess in s for s in WordList):
            print('Right!')
            for Letter in range(0, len(WordList)):
                if Guess == WordList[Letter]:
                    PlayersGuess[Letter] = Guess
        else:
            WrongCount -= 1
            print('Wrong, You have ', WrongCount, 'Changes left!')
        if not any('_' in s for s in PlayersGuess):
            print('\n\n\n', HANGMANPICS[7])
            print('\n\n You WIN!!!')
            break
        elif not WrongCount:
            print('\nYou Lose The word was', Word)
            print(HANGMANPICS[6])
            break


if __name__ == "__main__":
    HangMan()
