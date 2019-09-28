# based on https://www.reddit.com/r/beginnerprojects/comments/1dbena/challenge_whats_my_number/
# By Pete Baus 9/27/2019


def PrimeTest(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True  # is prime
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


Newlist = []
Numberlist = []
Numberlist.extend(range(1, 1001))

for Number in (range(8, -1, -1)):
    Numberlist.pop(Number)


for Number in Numberlist:
    if PrimeTest(Number):
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []
for Number in Numberlist:
    if not any([('1' in str(Number)), ('7' in str(Number))]):
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []
for Number in Numberlist:
    num = list(str(Number))
    num = [int(x) for x in num]
    if sum(num) <= 10:
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []
for Number in Numberlist:
    num = list(str(Number))
    num = [int(x) for x in num]
    if not ((num[0] + num[1]) % 2) == 0:
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []
for Number in Numberlist:
    num = list(str(Number))
    num = [int(x) for x in num]
    if (num[-2] % 2) == 0:
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []

for Number in Numberlist:
    num = list(str(Number))
    num = [int(x) for x in num]
    if (num[-1]) == len(num):
        Newlist.append(Number)
Numberlist = Newlist
Newlist = []


print(Numberlist)
