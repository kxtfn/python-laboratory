sentence = input("Введіть речення: ")
words = sentence.split()
unique = [w for w in words if words.count(w) == 1]
print("Слова, які зустрічаються один раз:", unique)
