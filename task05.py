# Задача 10
# Найти количество цифр 5 в числе
#     Пример:
#         543231235643
#         'В числе 2 5-ки.'

numbers = int(input('Введите произвольное число:'))
counter = 0
last_dig = 0
while numbers > 0:
    last_dig = numbers%10
    if last_dig == 5:
        counter += 1
    numbers = numbers//10

print('Количество пятёрок в числе:', counter)

