# # Вложенные списки
# # matrix =[
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# # ]
#
# N = 3
# matrix = [[i] * N for i in range(N)]
# print(matrix)
#
# # обход 2-мерного списка (матрицы)
# count = 1
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         matrix[row][col] = count
#         count += 1
#
# print(matrix)

matrix = []
table = []

star = 1
N = 8

for i in range(N):
    for j in range(star, star + N):
        table.append(j)
    matrix.append(table)
    table = []
    star += N

print(matrix)