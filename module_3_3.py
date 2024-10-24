def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params(b, c) # выдает ошибку
#print_params() # выводит в консоль: 1 строка True
# print_params(5) # выводит в консоль: 5 строка True
# print_params(c = [1,2,3]) # выводит в консоль: 1 строка [1, 2, 3]
# print_params(b = 25) # выводит в консоль: 1 25 True
values_list_ = [2, 42]
values_dict = {'a':3, 'b': 'мир', 'c': False}

print_params(*values_list_) # распаковывает: 2 42 True
print_params(**values_dict) # распаковывает: 3 мир False

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2,42) # распаковывает 54.32 Строка 42
