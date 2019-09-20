# based on https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/
# By Pete Baus 9/18/2019
import random


def GuessStep():
    print('\nHow to play: The computer randomly selects a number between 1 and 100 and the you has to guess what the number is. \nAfter every guess, the computer will tell you if the guess is higher or lower than the answer.\n')
    NumbberGuess = 0
    loop = True
    Answer = random.randint(1, 100)
    while loop == True:
        Guess = (int(input('what your guess? ')))
        if Guess > Answer:
            print('Too hight')
            NumbberGuess += 1
        elif Guess < Answer:
            print('Too Low')
            NumbberGuess += 1
        elif Guess == Answer:
            print('Thats right! it took you', NumbberGuess, 'Guess!')
            loop = False


def Call():
    loop2 = True
    while loop2 == True:
        GuessStep()
        Agin = input('Would you like to play agin? Y/n: ')
        if Agin in ['N', 'n', 'no', 'No']:
            loop2 = False


if __name__ == "__main__":
    Call()
