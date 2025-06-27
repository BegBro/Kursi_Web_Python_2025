"""
word = 'статор'
res = ''
for i in range(len(word)):
    res += word[i]*(i+1)
print(res)
"""

word = 'статор'
for i in range(len(word)):
    print(word[i]*(i+1), end= '')
