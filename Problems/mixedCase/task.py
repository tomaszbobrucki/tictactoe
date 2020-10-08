words = input().split()
word1 = [words[0]]
word2 = [words[i].capitalize() for i in range(1, len(words))]
word1.extend(word2)
print("".join(word1))
