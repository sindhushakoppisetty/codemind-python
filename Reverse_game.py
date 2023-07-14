def pal(n):
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
        l1.append(pal(l[i]))
print(*l1)
        