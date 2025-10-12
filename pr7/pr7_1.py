lines = [
    "Садок вишневий коло хати, хрущі над вишнями гудуть.",
    "Еней був парубок моторний.",
    "Матері вечерять ждуть, сім'я вечеря коло хати.",
    "Давно уже вона хотіла, Його щоб душка полетіла."
]

with open("TF16_1.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

golosni = "АЕИІОУЄЯЮЇаеииоуюєяї"
golosni_slova = []

with open("TF16_1.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')
    words = text.split()
    for word in words:
        if word and word[0] in golosni:
            golosni_slova.append(word)

with open("TF16_2.txt", "w", encoding="utf-8") as f2:
    for word in golosni_slova:
        f2.write(word + "\n")

with open("TF16_2.txt", "r", encoding="utf-8") as f2:
    for line in f2:
        print(line.strip())
