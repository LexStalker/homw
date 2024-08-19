numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0  # Проверяемое число
primes = []
not_primes = []
i = 0   # задаём счётчик
for i in range(len(numbers)):
    isprime = True
    n = numbers[i]
    if n < 2:
        continue
    else:

        f = n ** (1 / 2) # Квадратный корень из n
    for a in range(2, int(f +1)):
        if n % a == 0:
            isprime = False
            break

    if not (isprime):
        not_primes.append(n)
    else:
        primes.append(n)
isprime = True
print(primes)
print(not_primes)