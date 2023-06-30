a=int(input())
for i in range(int(a**0.5),a):
    if(i*(i+1))==a:
        print('YES')
        break
else:
    print('NO')