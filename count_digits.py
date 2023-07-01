s=input()
n=list(map(int,input().split()))
for i in n:
    print(len(str(abs(i))),end=" ")