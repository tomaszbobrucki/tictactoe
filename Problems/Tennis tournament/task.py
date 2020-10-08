n = int(input())

name = [input().split() for _ in range(0, n)]
winners = [na[0] for na in name if na[1] == "win"]
# print(name)
print(winners)
print(len(winners))
