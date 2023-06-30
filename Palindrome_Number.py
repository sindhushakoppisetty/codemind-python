n=int(input())
for i in range(n):
    n=int(input())
    m=n
    rev=0
    while n>0:
        r=n%10
        rev=10*rev+r
        n=n//10
    if(m==rev):
        print("True")
    else:
        print("False")