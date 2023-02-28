n = int(input('Enter a number: '))
def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = i * factorial
        print('The factorial of ',i,' is ' ,factorial)
fact(n)