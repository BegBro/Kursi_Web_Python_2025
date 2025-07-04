# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org) # Сайт библиотек для Python
# Графика
# PIL - Python Imagine Library
# pip freeze > requirements.txt - создания файла зависимости
# pip install -r requirements.txt - установка списка всех библиотек из txt (-r) - read
from PIL import Image
# image = Image.open('Images/doberman.jpg')
x,y = image.size
mode = image.mode
pixels = image.load() # загрузить таблицу пикселей

print(f'Ширина = {x}, высота = {y}')
print(f'Цветовая схема : {mode}')



# image_rotate = image.rotate(270)
# image_flip = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# cropped = image.crop((250,125,650,525))
# resized = image.resize((400,300))

# # Grayscale
# for i in range(x):
#     for j in range(y):
#         r,g,b = pixels[i,j]
#         average = (r+g+b) // 3
#         pixels[i,j] = average,average,average

# # Негатив
# for i in range(x):
#     for j in range(y):
#         r,g,b = pixels[i,j]
#         pixels[i,j] = 255-r,255-g,255-b

# # Инверсия+-
# for i in range(x):
#     for j in range(y):
#         r,g,b = pixels[i,j]
#         pixels[i,j] = g,b,r

resized.save('Images/doberman2.jpg')
