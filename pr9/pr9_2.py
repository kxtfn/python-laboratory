import json

filename = 'rist.json'

def load_data():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Помилка відкриття файлу: {e}")
        return []

def save_data(data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def show_data(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))

def add_record(data):
    name = input("Введіть ім'я: ")
    gender = input("Введіть стать (чоловік/жінка): ")
    height = int(input("Введіть зріст (см): "))
    data.append({"name": name, "gender": gender, "height": height})

def delete_record(data):
    name = input("Введіть ім'я для видалення: ")
    data[:] = [item for item in data if item.get('name') != name]

def search_data(data):
    field = input("За яким полем шукати? (name/gender/height): ")
    value = input("Значення для пошуку: ")
    if field == 'height':
        value = int(value)
    results = [item for item in data if str(item.get(field)) == str(value)]
    show_data(results)

def avg_male_height(data):
    males = [item['height'] for item in data if item.get('gender') == 'чоловік']
    if males:
        avg = sum(males) / len(males)
        print(f"Середній зріст чоловіків: {avg:.2f} см")
        with open('avg_male_height.json', 'w', encoding='utf-8') as f:
            json.dump({"average_male_height": avg}, f, ensure_ascii=False, indent=2)
    else:
        print("Даних про чоловіків немає!")

def main():
    data = load_data()
    while True:
        print("\nМеню:")
        print("1 - Показати дані")
        print("2 - Додати")
        print("3 - Видалити")
        print("4 - Пошук")
        print("5 - Середній зріст чоловіків")
        print("0 - Вийти")
        choice = input("Вибір: ")
        if choice == '1':
            show_data(data)
        elif choice == '2':
            add_record(data)
            save_data(data)
        elif choice == '3':
            delete_record(data)
            save_data(data)
        elif choice == '4':
            search_data(data)
        elif choice == '5':
            avg_male_height(data)
        elif choice == '0':
            break
        else:
            print("Невірний вибір!")

if __name__ == '__main__':
    main()
