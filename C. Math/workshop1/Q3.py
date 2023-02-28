num = int(input('Enter a positive integer: '))
if num < 0:
    print(num,' is not a positive integer')
else:
    for i in range(1,num+1):
        multiples = 6 * i
        print("6 * ",i ," = ",multiples)