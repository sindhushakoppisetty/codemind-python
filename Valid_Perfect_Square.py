t=int(input())
for i in range(t):
    f=0
    n=int(input())
    for j in range(n):
        if(n==j*j):
            f=1
    if(f==1):
        print("True")
    else:
        print("False")