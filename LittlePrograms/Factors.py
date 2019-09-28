# based on https://www.reddit.com/r/beginnerprojects/comments/1a0d82/function_factors_of_a_number/
# By Pete Baus 9/28/2019
Number = int(input('What is your number?: '))
NumberList = []
for Num in range(1, Number):
    if (Number % Num) == 0:
        NumberList.append(Num)
NumberList.append(Number)
print('Your Factors are', NumberList)
