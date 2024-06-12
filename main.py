path = "books/frankenstein.txt"

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
    count_sort = sorted(count_list, key=lambda letter: letter[1], reverse=True)
    return count, count_sort

def report(count_words,count_sort):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in this document")
    for let in count_sort:
        letter = let[0]
        num = let[1]
        check = letter.isalpha()
        if check == True:
            print(f"The {letter} character was found {num} times")
        else:
            pass
    print("--- End Report ---")

def get_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

file_contents = get_book(path)
count_words, words = word_count(file_contents)
count_lets, count_sort = let_count(words)
report(count_words, count_sort)