def repeat_letters(text):
    s = set(text)
    result = set()
    for ch in s:
        if ch.isalpha() and text.count(ch) >= 2:
            result.add(ch)
    print("Літери, що зустрічаються не менше двох разів:", result)

t = input("Введіть текст з латинських літер: ")
repeat_letters(t)
