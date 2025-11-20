import pandas as pd
import numpy as np

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

additional_data = {
    "Аксьонов": {"вік": 22, "вага": 78, "зарплата": 15000, "відділ": "IT"},
    "Дмитренко": {"вік": 24, "вага": 72, "зарплата": 18000, "відділ": "Маркетинг"},
    "Чесной": {"вік": 21, "вага": 65, "зарплата": 12000, "відділ": "HR"},
    "Годун": {"вік": 26, "вага": 85, "зарплата": 22000, "відділ": "IT"},
    "Письмак": {"вік": 20, "вага": 58, "зарплата": 11000, "відділ": "Бухгалтерія"},
    "Бобошко": {"вік": 25, "вага": 75, "зарплата": 19000, "відділ": "IT"},
    "Кузьменко": {"вік": 23, "вага": 62, "зарплата": 16000, "відділ": "Маркетинг"},
    "Рубан": {"вік": 22, "вага": 68, "зарплата": 13500, "відділ": "HR"},
    "Білоусов": {"вік": 19, "вага": 55, "зарплата": 10500, "відділ": "Бухгалтерія"},
    "Пилипчук": {"вік": 27, "вага": 67, "зарплата": 21000, "відділ": "IT"}
}

people_extended = {}
for surname, info in people.items():
    people_extended[surname] = {**info, **additional_data[surname]}

df = pd.DataFrame.from_dict(people_extended, orient='index')
df.index.name = 'прізвище'
df = df.reset_index()

print("=" * 80)
print("ВМІСТ СЛОВНИКА (DATAFRAME)")
print("=" * 80)
print(df)
print("\n")

print("=" * 80)
print("1. ПЕРШІ 3 РЯДКИ DATAFRAME")
print("=" * 80)
print(df.head(3))
print("\n")

print("=" * 80)
print("2. ТИПИ ДАНИХ")
print("=" * 80)
print(df.dtypes)
print("\n")

print("=" * 80)
print("3. РОЗМІР DATAFRAME (рядки × стовпці)")
print("=" * 80)
print(f"Кількість рядків: {df.shape[0]}")
print(f"Кількість стовпців: {df.shape[1]}")
print(f"Розмір: {df.shape}")
print("\n")

print("=" * 80)
print("4. ОПИСОВА СТАТИСТИКА")
print("=" * 80)
print(df.describe())
print("\n")

print("=" * 80)
print("5. ДОДАВАННЯ РОЗРАХУНКОВИХ СТОВПЦІВ")
print("=" * 80)

df['IMT'] = (df['вага'] / ((df['зріст'] / 100) ** 2)).round(2)

df['річний_дохід'] = df['зарплата'] * 12

def age_category(age):
    if age < 21:
        return 'молодший'
    elif age < 25:
        return 'середній'
    else:
        return 'старший'

df['категорія_віку'] = df['вік'].apply(age_category)

print("Додано стовпці: 'IMT', 'річний_дохід', 'категорія_віку'")
print(df[['прізвище', 'ім\'я', 'IMT', 'річний_дохід', 'категорія_віку']].head())
print("\n")

print("=" * 80)
print("6. ФІЛЬТРАЦІЯ: Люди із зарплатою понад 15 000 грн")
print("=" * 80)
filtered_df = df[df['зарплата'] > 15000]
print(filtered_df[['прізвище', 'ім\'я', 'зарплата', 'відділ', 'річний_дохід']])
print(f"\nЗнайдено осіб: {len(filtered_df)}")
print("\n")

print("=" * 80)
print("7. ФІЛЬТРАЦІЯ: Чоловіки зі зростом більше 170 см")
print("=" * 80)
filtered_tall_men = df[(df['стать'] == 'чоловік') & (df['зріст'] > 170)]
print(filtered_tall_men[['прізвище', 'ім\'я', 'зріст', 'стать']])
print(f"\nЗнайдено осіб: {len(filtered_tall_men)}")
print("\n")

print("=" * 80)
print("8. СОРТУВАННЯ: За спаданням зарплати")
print("=" * 80)
sorted_salary = df.sort_values('зарплата', ascending=False)
print(sorted_salary[['прізвище', 'ім\'я', 'зарплата', 'відділ', 'річний_дохід']].head(10))
print("\n")

print("=" * 80)
print("9. СОРТУВАННЯ: За зростанням віку")
print("=" * 80)
sorted_age = df.sort_values('вік', ascending=True)
print(sorted_age[['прізвище', 'ім\'я', 'вік', 'категорія_віку', 'зарплата']])
print("\n")

print("=" * 80)
print("10. СОРТУВАННЯ: За зростом (спадання)")
print("=" * 80)
sorted_height = df.sort_values('зріст', ascending=False)
print(sorted_height[['прізвище', 'ім\'я', 'зріст', 'вага', 'IMT']].head(10))
print("\n")

print("=" * 80)
print("11. ГРУПУВАННЯ: Середні значення за відділами")
print("=" * 80)
grouped_dept = df.groupby('відділ').agg({
    'зарплата': 'mean',
    'вік': 'mean',
    'зріст': 'mean',
    'вага': 'mean',
    'річний_дохід': 'mean'
}).round(2)
print(grouped_dept)
print("\n")

print("=" * 80)
print("12. ГРУПУВАННЯ: Середні значення за статтю")
print("=" * 80)
grouped_gender = df.groupby('стать').agg({
    'зарплата': 'mean',
    'вік': 'mean',
    'зріст': 'mean',
    'вага': 'mean',
    'IMT': 'mean'
}).round(2)
print(grouped_gender)
print("\n")

print("=" * 80)
print("13. ГРУПУВАННЯ: Середні значення за категорією віку")
print("=" * 80)
grouped_age_cat = df.groupby('категорія_віку').agg({
    'зарплата': 'mean',
    'зріст': 'mean',
    'вага': 'mean'
}).round(2)
print(grouped_age_cat)
print("\n")

print("=" * 80)
print("14. АГРЕГАЦІЯ: Максимальна зарплата у кожному відділі")
print("=" * 80)
max_salary_dept = df.groupby('відділ')['зарплата'].max().sort_values(ascending=False)
print(max_salary_dept)
print("\n")

print("=" * 80)
print("15. АГРЕГАЦІЯ: Мінімальна та максимальна зарплата за статтю")
print("=" * 80)
salary_range_gender = df.groupby('стать')['зарплата'].agg(['min', 'max', 'mean']).round(2)
print(salary_range_gender)
print("\n")

print("=" * 80)
print("16. АГРЕГАЦІЯ: Кількість осіб у кожному відділі")
print("=" * 80)
count_dept = df['відділ'].value_counts()
print(count_dept)
print("\n")

print("=" * 80)
print("17. АГРЕГАЦІЯ: Кількість унікальних імен")
print("=" * 80)
unique_names = df['ім\'я'].nunique()
print(f"Кількість унікальних імен: {unique_names}")
print("\nУсі унікальні імена:")
print(df['ім\'я'].unique())
print("\n")

print("=" * 80)
print("18. АГРЕГАЦІЯ: Загальний фонд зарплат за відділами")
print("=" * 80)
total_salary_dept = df.groupby('відділ')['зарплата'].sum().sort_values(ascending=False)
print(total_salary_dept)
print("\n")

print("=" * 80)
print("АНАЛІЗ ЗАВЕРШЕНО")
print("=" * 80)