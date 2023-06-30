n=int(input())
p=0
s=n*n
while(s):
    c=s%10
    p=p+c
    s=s//10
if(p==n):
    print("Neon Number")
else:
    print("Not Neon Number")