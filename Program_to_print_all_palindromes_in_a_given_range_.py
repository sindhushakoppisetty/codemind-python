a=int(input())
b=int(input())
for i in range(a,b+1):
    a=str(i)
    if a==a[::-1]:
        print(a,end=' ')