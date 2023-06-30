h,s,sp=map(int,input().split())
a=h>50
b=s>60
c=sp>100
if(a==True and b==True and c==True):
    print(10)
elif(a==True and b ==True):
    print(9)
elif(b==True and c==True):
    print(8)
elif(a==True and c ==True):
    print(7)
elif(a==False and b==False and c==False):
    print(5)
else:
    print(6)