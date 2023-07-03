n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
for i in a:
    if a.count(i)!=1:
        c+=1
        s.append(i)
j=set(s)
print(*j)