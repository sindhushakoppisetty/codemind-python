a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
s=[]
for i in c:
    if i in d:
        if i not in s:
            s.append(i)
print(len(s))