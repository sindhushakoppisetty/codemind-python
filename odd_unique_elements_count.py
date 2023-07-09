n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in l:
    if i not in lst:
        if i%2!=0:
            lst.append(i)
print(len(lst))