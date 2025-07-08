# res = []
# with open('info.txt', 'rt') as f:
#    while temp := f.readline().rstrip('\n'):
#        res += temp.split(', ')
#
# # res = set(list(map(lambda x: x.rstrip('\n'),res)))
# # res = set(res)
# res = sorted(int(x) for x in set(res))
#
# print(res)
from path_lib import *
print(img_dir)

# import pickle
# import pprint

# d = {
#     'стол': 'table',
#     'стул': 'chair',
# }

# # Сериализация
# with open('dictfile.dat', 'wb') as p:
#     # d - что сериализуем
#     # p - куда сериализуем
#     pickle.dump(d, p)

# # Десериализация
# with open('dictfile.dat', 'rb') as p:
#     d = pickle.load(p)
# pprint.pprint(d,width=15)

