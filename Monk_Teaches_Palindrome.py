n=int(input())
for i in range(n):
    a=input()
    c=0
    b=a[::-1]
    if a==b:
        for j in a:
            c+=1
        if c%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')