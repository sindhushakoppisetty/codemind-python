s=input()
n=s.replace(" ","")
c=0
for i in s:
    if i in n:
        c+=1
print(c)