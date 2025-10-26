with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()
word_count = len(words)
print(f"Общее количество слов в статье: {word_count}")
word_freq = {}
for word in words:
    cleaned_word = word.strip('.,!?;:"?()').lower()
    if cleaned_word:
        if cleaned_word in word_freq:
            word_freq[cleaned_word] += 1
        else:
            word_freq[cleaned_word] = 1
most_common_word = max(word_freq, key=word_freq.get)
most_common_count = word_freq[most_common_word]

print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")