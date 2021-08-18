num = int(input('Введите любое целое положительное число'))
max_num = 0
while num > 10:
    if num % 10 > max_num:
        max_num = num % 10
        if max_num == 9:
            break
    num = num // 10

print(f'Наибольшая цифра числа: {max_num}')
