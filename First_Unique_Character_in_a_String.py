s=input()
flag=1
l=[]
for i in s:
    if s.count(i)==1:
        flag=0
        l.append(s.index(i))
if flag==0:
    print(l[0])
else:
    print("-1")