import sys

data = [d.strip('\n') for d in sys.stdin.readlines()]
words = []
len_3lines = 0
res = []
for i in range(0, len(data) - len(data) % 3, 3):
    lines_3 = data[i:i + 3]
    print(lines_3)
    for line in lines_3:
        len_3lines += len(line)
    par = (len_3lines % 2 == 0)
    for line in lines_3:
        words.extend(line.split())
    even_words = [word for word in words if (len(word) % 2 == 0) == par]
    for word in even_words:
        word.lower()
    sort_words = sorted(set(even_words))
    res_words = sort_words[:5]

print(res_words)