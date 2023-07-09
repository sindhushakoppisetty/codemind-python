n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    for i in range(n+1):
        l.append(0)
        break
print(*l)