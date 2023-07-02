n=int(input())
m=n
s=0
while(n):
    i=1
    fac=1
    r=n%10
    while(i<=r):
        fac=fac*i
        i=i+1
    s=s+fac
    n=n//10
if(s==m):
    print('The number',m,'is a strong number')
else:
    print('The number',m,'is not a strong number')