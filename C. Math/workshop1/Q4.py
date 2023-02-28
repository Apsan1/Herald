def prime():
    n = int(input('Enter a number: '))
    if n == 2 or n == 3:
        print('It is a prime number')
    else:
        if n % 2 == 0 or n% 3 == 0:
            print('It is not a prime number.')
        else:
            print('It is a prime number')
prime()