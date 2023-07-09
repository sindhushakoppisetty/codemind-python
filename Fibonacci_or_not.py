n=int(input())
a=0
b=1
for i in range(n-2):
    s=a+b
    if s==n:
        print("True")
        break
    a=b
    b=s
else:
    print("False")