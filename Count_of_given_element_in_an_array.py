n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
for i in a:
    if i==m:
        c=c+1
print(c)
    