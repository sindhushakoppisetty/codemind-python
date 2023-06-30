a=input()
if '-' in a:
    print(int('-'+a[:0:-1]))
else:
    print(int(a[::-1]))