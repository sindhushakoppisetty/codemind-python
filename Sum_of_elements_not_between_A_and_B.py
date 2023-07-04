a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
for i in l:
    if i<b or i>c:
        d+=i
print(d)