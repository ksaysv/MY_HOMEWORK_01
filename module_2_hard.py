import random

number = random.randint(3, 20)
print(number)
code = range(1, number)
a = str()
for i in code:
    for j in range(i+1, number):
        if number % (j+i) == 0:
            a = a + str(i) + str(j)
        else:
            continue
print('result: ',a)