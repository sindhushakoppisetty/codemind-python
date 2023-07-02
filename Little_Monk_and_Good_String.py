n=input()
s=list(n)
s1="AEIOUaeiou"
c=0
m=0
for i in s:
    if i in s1:
        c+=1
        if m<=c:
            m=c
    else:
        c=0
print(m)