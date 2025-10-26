with open('input.txt', 'r', encoding='utf-8') as file:
    banned_words = file.read().split()
text = input("Введите предложение: ")
print("\nИсходный текст:")
print(text)
result = text
for banned_word in banned_words:
    start = 0
    while True:
        index = result.lower().find(banned_word.lower(), start)
        if index == -1:
            break
        word_length = len(banned_word)
        result = result[:index] + '*' * word_length + result[index + word_length:]
        start = index + word_length

print("\nРезультат после замены:")
print(result)