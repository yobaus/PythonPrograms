# based on https://www.reddit.com/r/beginnerprojects/comments/2agwnq/project_multiplication_table/
# By Pete Baus 9/19/2019


Size = (int(input('How Large?: '))) + 1
Numbers = (list(range(0, Size)))
TableNumber = Numbers
count = 0

for Number in Numbers:
    for SubNumber in Numbers:
        # TableNumber.append(Number * SubNumber)
        # rjust set the pading on the numbers
        print(str(Number * SubNumber).rjust(6, ' '), end='')
        count += 1
        if count == Size:
            print(' ', flush=True)
            count = 0
