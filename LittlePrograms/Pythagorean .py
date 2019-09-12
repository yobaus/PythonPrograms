# based on https://www.reddit.com/r/beginnerprojects/comments/19jwi6/project_pythagorean_triples_checker/
# By Pete Baus 9/11/2019

Loop = True
def PartOne():
    print('Welcome to the right triangle  tester. \n*plese only you number key and whole numbers.')
    Side1 = int(input('Plese type your first side: ')) # input is a string so you have to you int to convert it to integer
    Side2 = int(input('Plese type your second side: '))
    Side3 = int(input('Plese type your third side: '))
    print (type(Side1), type(Side2), type(Side3))
    if Side1 > Side2 and Side1 > Side3:                  #Finds the hypotenuse
        RightTriangle = ((Side2)**2 + (Side3)**2 == (Side1)**2)
    elif Side2 > Side1 and Side2 > Side3:
        RightTriangle = ((Side1)**2 + (Side3)**2 == (Side2)**2)
    elif Side3 > Side2 and Side3 > Side1:
        RightTriangle = ((Side1)**2 + (Side2)**2 == (Side3)**2)
    else:
        RightTriangle = False #if one 
    if RightTriangle:
        print ('This is a right Triangle! ')
    else:
        print('This is not a right triangle! ')

def PartTwo():
    while Loop:
        PartOne()
        Again = input ('Would you like to do a new triangle? y/n: ' )
        if Again in ['n', 'N']:
            break

if __name__ == "__main__":
    PartTwo()