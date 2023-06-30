s=input()
b=" ".join(s)
c=0
for i in s:
    if i.isdigit():
        c+=int(i)
print(c)