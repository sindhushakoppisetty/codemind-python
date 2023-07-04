a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
for i in l:
    if i<b or i>c:
        d.append(i)
if len(d)>0:
    print(*d)
else:
    print("-1")