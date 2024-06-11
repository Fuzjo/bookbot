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
    return count

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
count_words, words = word_count(file_contents)
count_lets = let_count(words)
print(count_words, count_lets)