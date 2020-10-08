ne = [int(x) for x in input()]

a = []

new1 = [a.append(a[-1] + ne[x]) if x > 0 else a.append(ne[x]) for x in range(0, len(ne))]
print(a)
