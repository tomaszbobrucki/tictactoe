text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.lower().startswith("www.") or word.lower().startswith("https://") or word.lower().startswith("http://"):
        print(word)
