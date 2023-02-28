for i in range(1,21):
    n = i
    print('\n\nThe number is', n)
    def s1(n):
        sum_number = (n*(n+1))/2
        print('The sum of natural numbers is ',sum_number)
    def s2(n):
        sum_square = (n*(n+1)*((2*n)+1))/6
        print('The sum of square numbers is ',sum_square)
    s1(n)
    s2(n)