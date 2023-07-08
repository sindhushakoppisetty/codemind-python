def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
n=int(input())
c=0
for j in range(1,n+1):
    if n%j==0 and prime(j)==0:
        c=c+1
print(c)