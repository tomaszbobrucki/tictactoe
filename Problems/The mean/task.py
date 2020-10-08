numbers = list(input())

new_list = [float(x) for x in numbers]

all1 = 0
for i in new_list:
    all1 += i

print(all1 / len(new_list))
