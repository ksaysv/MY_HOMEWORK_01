# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# index = 0
# for i in range(2, len(numbers) + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             index = index + 1
#     if index == 0:
#         primes.append(i)
#     else:
#         index = 0
#         not_primes.append(i)
# print('primes:', primes)
# print('not_primes:', not_primes)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# for number in numbers:
#     if number == 1:
#         continue
#
#     is_prime = True
#     for divider in range(2, number // 2 + 1):
#         if number % divider == 0:
#             is_prime = not is_prime
#             break
#     if is_prime:
#         primes.append(number)
#     else:
#         not_primes.append(number)
#
# print(f'Primes: {primes}')
# print(f'Not Primes: {not_primes}')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            primes.append(number)
            break
    else:
        not_primes.append(number)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')