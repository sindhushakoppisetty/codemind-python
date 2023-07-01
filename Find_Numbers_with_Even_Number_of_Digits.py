a=input()
l=list(map(str,input().split()))
count=0
for i in l:
    if len(i)%2==0:
        count+=1
print(count)