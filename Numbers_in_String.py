s=input()
c="".join(s)
c1=list(c)
s=0
for i in c1:
    if i.isdigit():
        s+=int(i)
print(s)
