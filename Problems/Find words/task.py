words = input().split()

new1 = [word for word in words if word.endswith("s")]

print("_".join(new1))
