def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
c=0
k=int(input())
for i in l:
    if prime(i):
        if i>=k:
            c+=1
print(c)