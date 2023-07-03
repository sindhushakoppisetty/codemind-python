n=input()
s=list(n.lower())
l=[]
for i in s:
    if s.count(i)==1 and i!=" ":
        l.append(i)
d=sorted(l)
print("".join(d))