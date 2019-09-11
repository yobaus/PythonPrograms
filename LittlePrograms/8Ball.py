# based on https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/
# By Pete Baus 9/10/2019
import random
import time
Answers = (
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    " You may rely on it.",
)


def Magic():
    Looping = True
    while Looping == True:
        print("Welcome to the Magic 8 Ball")
        Q = input('Please ask a question or type "Q" quit: \n')
        if Q in ['Q', 'q']:
            print("Thanks for playing!")
            Looping = False
            break
        print('Let Me think about this....\n')
        time.sleep(3)
        if Q in ['Q', 'q']:
            Looping == False
        print(f'The answer to your question "{Q}" is.')
        R = random.randint(0, 20)
        print(Answers[R])
        time.sleep(5)


if __name__ == "__main__":
    Magic()
