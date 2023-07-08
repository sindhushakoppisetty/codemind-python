import math
def prime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=n+m
for i in range(1,20):
    if prime(c+i):
        print(i)
        break
