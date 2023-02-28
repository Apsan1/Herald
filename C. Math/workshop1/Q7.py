x = int(input('Enter a number: '))
n = int(input('Enter the power: '))
if n<0:
    print(n,'isnot a positive integer.')
else:
    def myPow(x,n):
        power = 1
        pow = n
        while n > 0:
            power = power * x
            n = n - 1
        print('The exponential power ',pow, 'of number ',x,' is ',power)

    myPow(x,n)
