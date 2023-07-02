n=int(input())
for i in range(n):
    a=int(input())
    fac=1
    while a:
        fac=fac*a
        a=a-1
    print(fac)