def longest_word(file):
    with open(file, encoding= "utf=8") as f:
        words = f.read().split()
        max_length = len(max(words, key = len))
        for word in words:
            if len(word) == max_length:
                sougth_words = word
        if len(sougth_words) == 1:
            return sougth_words[0]
        return sougth_words
print(longest_word("input2.txt"))