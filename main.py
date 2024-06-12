def word_count(file_contents):
    words = file_contents.split()
    count_word = len(words)
    return count_word, words

def let_count(words):
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
    count_list = list(count.items())
    count_sort = count_list.sort()
    print(count_sort)
    return count, count_sort

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
count_words, words = word_count(file_contents)
count_lets, count_sort = let_count(words)
print(count_words, count_lets)

print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{count_words} words found in this document")
for let in count_lets:
    letter = let[0]
    check = letter.isalpha()
    if check == True:
        print(f"The {letter} character was found {count_lets[f'{let}']} times")
    else:
        pass