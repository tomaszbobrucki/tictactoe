number = int(input())
max1 = number * 2 - 1
for i in range(1, number + 1):
    if i == 1:
        print("#".center(max1))
    else:
        print(("#" * (i * 2 - 1)).center(max1))
