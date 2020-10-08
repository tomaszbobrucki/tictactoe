prime_numbers = []

for i in range(2, 1001):
    new = [i % n != 0 for n in range(2, i)]
    # print(new)
    if all(new):
        prime_numbers.append(i)

# print(prime_numbers)
