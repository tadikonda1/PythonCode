
def fib(n):
    num=0
    a,b=0,1
    for i in range(n):
        a,b=b,(a+b)
        print (a)
        if a%2==0:
            num=num+a
            print("..")
            print(num)
            print("..")
    return num

print (fib(10))
