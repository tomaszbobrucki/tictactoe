# put your python code here
list1 = input().split()

total_a = 0

for let in list1:
    if let == "A":
        total_a += 1

print(round(total_a / len(list1), 2))
