n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    c+=i
res = "{:.2f}".format(c/n)
print(res)