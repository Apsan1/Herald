max = int(input('Enter the maximum odd number: '))
if max%2 == 0 or max < 0:
    print(max,' is not an odd or positive number')
else:
    sum = 0
    for i in range(1,max):
        if i%2 == 1:
            sum = sum + i
    print('The sum of odd numbers till ',max ,' is ',sum)