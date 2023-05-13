n=input()
s=list(n)
for i in s:
    if int(i)%2!=0:
        print(int(i)*int(i),end="")