n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if(ord(i)>=48 and ord(i)<=57):
            c+=1
    if(c==0):print("No")
    else:print("Yes")