numbers = list(input())
# print(numbers)

number1 = [int(nu) for nu in numbers]
# print(number1)

new1 = [(number1[num] + number1[num + 1]) / 2 for num in range(0, len(number1) - 1)]
print(new1)
