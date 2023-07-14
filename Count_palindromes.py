def pal(n):
    rev=0
    temp=n
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return rev
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i):
        c+=1
print(c)