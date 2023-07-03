def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))
str1=input()
print(check_isogram(str1))