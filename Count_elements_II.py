a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
s=[]
s1=[]
for i in c:
   if i not in d:
       s.append(i)
for i in d:
    if i not in c:
        s1.append(i)
s3=s+s1
s4=set(s3)
print(len(s4))