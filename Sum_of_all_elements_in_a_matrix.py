r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
se=[]
for i in range(r):
    se.append(sum(mat[i]))
print(sum(se))