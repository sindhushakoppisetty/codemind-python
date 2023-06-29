n=int(input())
temp=n
su=0
while n:
    r=n%10
    su=su*10+r
    n=n//10
m=su
s=su*su
rem=0
while s:
    r=s%10
    rem=rem*10+r
    s=s//10
if(temp*temp)==rem:
    print("True")
else:
    print("False")
