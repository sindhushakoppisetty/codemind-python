n=int(input())
s=list(map(int,input().split()))
m=int(input())
for i in s:
    if m==i:
        print("True")
        break
else:
    print("False")