n=int(input())
a=list(map(int,input().split()))
a1=set(a)
s=0
for i in a1:
    if(i%2==0):
        s+=1
print(s)