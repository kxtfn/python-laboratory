people = {
    "Аксьонов": {"ім'я": "Ігор", "зріст": 180, "стать": "чоловік"},
    "Дмитренко": {"ім'я": "Богдан", "зріст": 175, "стать": "чоловік"},
    "Чесной": {"ім'я": "Влад", "зріст": 165, "стать": "чоловік"},
    "Годун": {"ім'я": "Микола", "зріст": 182, "стать": "чоловік"},
    "Письмак": {"ім'я": "Архип", "зріст": 160, "стать": "чоловік"},
    "Бобошко": {"ім'я": "Вадим", "зріст": 178, "стать": "чоловік"},
    "Кузьменко": {"ім'я": "Карина", "зріст": 179, "стать": "жінка"},
    "Рубан": {"ім'я": "Богдан", "зріст": 167, "стать": "чоловік"},
    "Білоусов": {"ім'я": "Єгор", "зріст": 158, "стать": "чоловік"},
    "Пилипчук": {"ім'я": "Єлизавета", "зріст": 181, "стать": "жінка"}
}

def show_all_values(d):
    for key, value in d.items():
        print(f"{key}: {value}")

def add_entry(d, surname, name, height, gender):
    if surname in d:
        print("Запис з таким прізвищем вже існує.")
    else:
        d[surname] = {"ім'я": name, "зріст": height, "стать": gender}
        print(f"Запис додано: {surname}: {d[surname]}")

def delete_entry(d, surname):
    try:
        del d[surname]
        print(f"Запис зі словником {surname} видалено.")
    except KeyError:
        print(f"Запис з ключем '{surname}' не знайдено.")

def show_sorted(d):
    for key in sorted(d.keys()):
        print(f"{key}: {d[key]}")

def average_height_men(d):
    total_height = 0
    count = 0
    for person in d.values():
        if person["стать"] == "чоловік":
            total_height += person["зріст"]
            count += 1
    if count > 0:
        return total_height / count
    else:
        return None

print("Усі записи у словнику:")
show_all_values(people)

print("\nДодаємо нового запис:")
add_entry(people, "Лях", "Дмитро", 177, "чоловік")

print("\nВидаляємо запис з прізвищем 'Лях':")
delete_entry(people, "Лях")

print("\nЗаписи за відсортованими ключами:")
show_sorted(people)

avg_height = average_height_men(people)
if avg_height is not None:
    print(f"\nСередній зріст чоловіків: {avg_height:.2f} см")
else:
    print("\nЧоловіків у словнику немає.")