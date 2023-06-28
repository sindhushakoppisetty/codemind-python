n,m=map(int,input().split())
e=0
o=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in m:
        if i%2:
            o=o+i
        else:
            e=e+i
print(e,o)