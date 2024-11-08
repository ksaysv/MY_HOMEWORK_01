def calculate_structure_sum(item):
    total = 0
    if isinstance(item, (int, float)):
        total += item
    elif isinstance(item, str):
        total += len(item)
    elif isinstance(item, (list, tuple, set)):
        for i in item:
            total += calculate_structure_sum(i)
    elif isinstance(item, dict):
        for key, value in item.items():
            total = total + calculate_structure_sum(value) + calculate_structure_sum(key)
    return total

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
