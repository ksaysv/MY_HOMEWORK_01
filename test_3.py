import random

number = random.randint(3, 20)
print(number)
pass_Colona_2 = []
for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                a = i,j
                pass_Colona_2.append(a)
            else:
                continue
print(pass_Colona_2)
