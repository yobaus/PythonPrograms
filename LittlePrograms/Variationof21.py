# based on https://www.reddit.com/r/beginnerprojects/comments/19ot36/project_a_variation_of_21/
# By Pete Baus 11/7/2019

import random


class Cards:
    def __init__(self):
        self.Deck = [
            ["Ace of Spades", 1],
            ["2 of Spades", 2],
            ["3 of Spades", 3],
            ["4 of Spades", 4],
            ["5 of Spades", 5],
            ["6 of Spades", 6],
            ["7 of Spades", 7],
            ["8 of Spades", 8],
            ["9 of Spades", 9],
            ["10 of Spades", 10],
            ["Jack of Spades", 10],
            ["Queen of Spades", 10],
            ["King of Spades", 10],
            ["Ace of Hearts", 1],
            ["2 of Hearts", 2],
            ["3 of Hearts", 3],
            ["4 of Hearts", 4],
            ["5 of Hearts", 5],
            ["6 of Hearts", 6],
            ["7 of Hearts", 7],
            ["8 of Hearts", 8],
            ["9 of Hearts", 9],
            ["10 of Hearts", 10],
            ["Jack of Hearts", 10],
            ["Queen of Hearts", 10],
            ["King of Hearts", 10],
            ["Ace of Diamonds", 1],
            ["2 of Diamonds", 2],
            ["3 of Diamonds", 3],
            ["4 of Diamonds", 4],
            ["5 of Diamonds", 5],
            ["6 of Diamonds", 6],
            ["7 of Diamonds", 7],
            ["8 of Diamonds", 8],
            ["9 of Diamonds", 9],
            ["10 of Diamonds", 10],
            ["Jack of Diamonds", 10],
            ["Queen of Diamonds", 10],
            ["King of Diamonds", 10],
            ["Ace of Clubs", 1],
            ["2 of Clubs", 2],
            ["3 of Clubs", 3],
            ["4 of Clubs", 4],
            ["5 of Clubs", 5],
            ["6 of Clubs", 6],
            ["7 of Clubs", 7],
            ["8 of Clubs", 8],
            ["9 of Clubs", 9],
            ["10 of Clubs", 10],
            ["Jack of Clubs", 10],
            ["Queen of Clubs", 10],
            ["King of Clubs", 10],
        ]
        self.Deck += self.Deck
        self.Deck += self.Deck
        self.Hand = [self.PickCard(), self.PickCard()]
        self.RScore = 0
        self.GScore = 100

    def PickCard(self):
        __Card__ = self.Deck[random.randint(0, len(self.Deck)-1)]
        self.Deck.remove(__Card__)
        return __Card__

    def Deal(self):
        self.Hand = [self.PickCard(), self.PickCard()]
        self.RScore = 0

    def Hit(self):
        self.Hand.append((self.PickCard()))
        self.Count()

    def Count(self):
        self.RScore = 0
        for card in self.Hand:
            self.RScore += card[1]

    def Rank(self):
        if self.GScore >= 90:
            self.Rank = 'A'
        elif self.GScore >= 80:
            self.Rank = 'B'
        elif self.GScore >= 70:
            self.Rank = 'C'
        elif self.GScore <= 69:
            self.Rank = 'F'
        return self.Rank


def Game():
    Player = Cards()
    for i in range(1, 5):
        Loop = True
        Player.Deal()
        while Loop:
            print(f"Round {i}!!!")
            if Player.RScore >= 21:
                Player.GScore -= abs(21-Player.RScore)
                print(
                    f"Your Curent Hand is {Player.Hand}\nYour Score is {Player.RScore}\n\n\nYou Busted your Score This round is  {Player.RScore}, Your Game Score is curently {Player.GScore}")
                Loop = False
                continue
            Player.Count()
            print(
                f"Your Curent Hand is {Player.Hand}\nYour Score is {Player.RScore}")
            Choice = input('Hit or Stay: ')
            if Choice in ['Hit', 'hit', 'h', 'H']:
                Player.Hit()
            elif Choice in ['Stay', 'stay', 'S', 's']:
                Player.GScore -= abs(21-Player.RScore)

                print(
                    f"Your Score This round is  {Player.RScore}, Your Game Score is curently {Player.GScore}")
                Loop = False
                continue
    print(
        f"\n\n\nYour Finale Score Was {Player.GScore}!\n Your Rank is {Player.Rank()}!!!")


if __name__ == "__main__":
    Game()
