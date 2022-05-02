# Задача 9
# Найти максимальную цифру в числе


numbers = int(input('Введите произвольное число: '))

last_dig = 0
max_n = 0

while numbers > 0:
    last_dig = numbers%10
    if last_dig > max_n:
        max_n = last_dig
    numbers = numbers//10

print('Максимальная цифра введённого числа:', max_n)




