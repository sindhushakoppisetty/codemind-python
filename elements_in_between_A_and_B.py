n=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
flag=0
l=[]
for i in arr:
    if i>=n and i<=m:
        flag=1
        l.append(i)
if(flag==1):
    for i in l:
        print(i,end=" ")
else:
    print("-1")