n=int(input())
l=list(map(int,input().split()))
o=0
for i in range(1,len(l)-1):
    if l[i]%2!=0:
        if l[i-1]%2!=0 and l[i+1]%2!=0:
            o+=1
print(o)
    