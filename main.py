with open("books/frankenstein.txt") as f:
    file_contents = f.read()


words = file_contents.split()
count = len(words)
print(count)
letters = []
count = {}

for word in words:
    word = word.lower()
    for let in word:
        letters.append(let)
for let in letters:
    if let in count:
        count[let] += 1
    else:
        count[let] = 1
print(count)