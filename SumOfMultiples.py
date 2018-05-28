
def MultiplesOfNum(a):
    num=0;
    b=0;
    for l in range (0,10000):

        if (l%a)==0:
            num=num+(a*b);
            b=b+1;

    return num

result=0
a=MultiplesOfNum(10)
print (a)
print ("Multiples of 5 Done")
b=MultiplesOfNum(19)
print(b)
print ("Multiples of 3 Done")
result=a+b
print(result)









