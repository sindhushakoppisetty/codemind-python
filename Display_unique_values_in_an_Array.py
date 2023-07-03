n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in l:
    if l.count(i)==1:
        c+=1
        s.append(i)
if c:
    print(*s)
else:
    print("-1")
        
