with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()
clean_words = []
for word in words:
    clean_word = word.strip('.,!?;:"()')
    if clean_word:
        clean_words.append(clean_word)
clean_words.sort(key=len, reverse=True)
longest_words = clean_words[:3]
print("Три самых длинных слова в тексте:")
for i, word in enumerate(longest_words, 1):
    print(f"{i}. '{word}' (длина: {len(word)} символов)")
with open('longest_words.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("Три самых длинных слова:\n")
    for i, word in enumerate(longest_words, 1):
        output_file.write(f"{i}. {word} - {len(word)} символов\n")
print("\nРезультат также сохранен в файл 'longest_words.txt'")