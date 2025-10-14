lines = [
    "Садок вишневий коло хати, хрущі над вишнями гудуть.",
    "Еней був парубок моторний.",
    "Матері вечерять ждуть, сім'я вечеря коло хати.",
    "Давно уже вона хотіла, Його щоб душка полетіла."
]

try:
    with open("TF16_1.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
except IOError as e:
    print(f"Помилка при записі у файл TF16_1.txt: {e}")

golosni = "АЕИІОУЄЯЮЇаеииоуюєяї"
golosni_slova = []

try:
    with open("TF16_1.txt", "r", encoding="utf-8") as f:
        text = f.read()
        text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')
        words = text.split()
        for word in words:
            if word and word[0] in golosni:
                golosni_slova.append(word)
except IOError as e:
    print(f"Помилка при читанні файлу TF16_1.txt: {e}")

try:
    with open("TF16_2.txt", "w", encoding="utf-8") as f2:
        for word in golosni_slova:
            f2.write(word + "\n")
except IOError as e:
    print(f"Помилка при записі у файл TF16_2.txt: {e}")

try:
    with open("TF16_2.txt", "r", encoding="utf-8") as f2:
        for line in f2:
            print(line.strip())
except IOError as e:
    print(f"Помилка при читанні файлу TF16_2.txt: {e}")
