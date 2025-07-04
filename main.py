# import sys
#
# data = [d.strip('\n') for d in sys.stdin.readlines()]
# words = []
# len_3lines = 0
# res = []
# d = []
# for i in range(0, len(data) - len(data) % 3, 3):
#     lines_3 = data[i:i + 3]
#     print(lines_3)
#     for line in lines_3:
#         len_3lines += len(line)
#     par = (len_3lines % 2 == 0)
#     for line in lines_3:
#         words.extend(line.split())
#     even_words = [word for word in words if (len(word) % 2 == 0) == par]
#     for word in even_words:
#         d.append(word.lower())
#
#     sort_words = sorted(set(d))
# print(even_words)
# print(sort_words)



import sys
data = [d.strip('\n') for d in sys.stdin.readlines()]
length = len(data)
rem = length % 3

if rem:
    data = data[:length - rem]

for x in range(0,length - rem,3):
    summ = sum(len(a) for a in data[x:x + 3])
    result = []
    for s in data[x:x + 3]:
        temp = s.lower().split()
        result += filter(lambda a: len(a) % 2 == summ % 2, temp)
    result = sorted(set(map(lambda b: b.capitalize(),result)))[:5]
    print(*result, sep='. ')
