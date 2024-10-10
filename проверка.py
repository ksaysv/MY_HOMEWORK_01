# a = int(input('Введите число: '))
# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)
# a = int(input('Введите число: '))
# d = int(input('Введите число: '))
# n = int(input('Введите число: '))
# print(a*(d**(n-1)))
# a = int(input('Введите число: '))
# print(a,'---',a*2
# print(""Hello, it's me!"")"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    if my_list[index] < 0:
        break
    if my_list[index] == 0:
        index += 1
        continue
    print(my_list[index])
    index += 1


