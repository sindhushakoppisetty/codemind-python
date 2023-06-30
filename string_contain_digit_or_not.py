a=input()
count=0
for i in a:
    if i.isdigit():
        count+=1
if(count):
    print('Contains',count,'digit')

else:
    print('Doesn't contain digit')