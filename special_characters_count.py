s=input()
b='abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
c=0
for i in s:
    if i not in b:
        c+=1
print(c)