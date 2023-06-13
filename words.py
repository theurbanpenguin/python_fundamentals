#!/usr/bin/env python3
word = 'andrew'
word_length = len(word)
for l in word:
    print(l)
# range (start,end,step)
for l in range(word_length-1, -1, -1):
    #end='' Instead of normal newline print as a null string so we get all the letters on one line
    print(word[l], end='')
print()