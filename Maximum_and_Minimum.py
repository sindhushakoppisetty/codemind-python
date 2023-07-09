n=int(input())
l=list(map(int,input().split()))
s=0
s1=min(l)
c=0
for i in l:
    s2=l.count(i)
    if s2==i:
        c=1
        if s<i:
            s=i
        if s1>i:
            s1=i
if c==1:
    print(s1,s)
else:
    print("-1")