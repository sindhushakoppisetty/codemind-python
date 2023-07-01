def sort(s):
    words=s.split()
    words.sort(key=lambda word: (len(word),word))
    return words
s=input()
sw=sort(s)
print(*sw)