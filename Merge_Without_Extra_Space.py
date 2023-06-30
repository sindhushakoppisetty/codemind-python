for i in range(int(input())):
    a,b=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    s=arr1+arr2
    s.sort()
    print(*s)