a=input()
count=0
for i in a:
    if ord(i)<91:
        count+=1

    if ord(a[0])>94:
        count+=1
print(count)