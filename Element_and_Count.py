n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in l:
    m=l.count(i)
    if i not in lst:
        lst.append(i)
        if i in lst:
            print(i,m,end=" ")