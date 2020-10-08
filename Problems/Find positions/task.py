# put your python code here
num = input().split()
number = input()

n = num.count(number)
only = [str(i) for i in range(len(num)) if num[i] == number]
# print(only)

if len(only) > 0:
    print(" ".join(only))
else:
    print("not found")
