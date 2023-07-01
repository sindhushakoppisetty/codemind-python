a=int(input())
b=list(map(int,input().split()))
sum=0
index=0
for i in b:
    if index%2==0:
        sum-=i
    else:
        sum+=i
    index+=1
if(sum==0):
    print('YES')
else:
    print('NO')
