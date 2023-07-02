n=input()
s=list(n)
z=0
o=0
for i in s:
    if i=='z':
        z+=1
    elif i=='o':
        o+=1
if z*2==o:
    print('Yes')
else:
    print('No')