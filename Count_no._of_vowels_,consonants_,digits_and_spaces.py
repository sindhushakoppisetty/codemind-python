a=list(input())
vowel=0
const=0
space=0
digit=0
for i in a:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        vowel+=1
    elif i in ['1','2','3','4','5','6','7','8','9','0']:
        digit+=1
    elif i in ' ':
        space+=1
    else:
        const+=1
print('Vowels:',vowel)
print('Consonants:',const)
print('Digits:',digit)
print('White spaces:',space)