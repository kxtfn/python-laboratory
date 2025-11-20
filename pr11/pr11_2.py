import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'comptagevelo20152.csv')

df = pd.read_csv(csv_path)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

bike_columns = [col for col in df.columns if col != 'Date']

for col in bike_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

print("=" * 80)
print("1. ПЕРЕГЛЯД ПЕРШИХ РЯДКІВ ДАТАФРЕЙМУ")
print("=" * 80)
print(df.head())

print("\n" + "=" * 80)
print("2. ІНФОРМАЦІЯ ПРО ДАТАФРЕЙМ")
print("=" * 80)
print(df.info())

print("\n" + "=" * 80)
print("3. СТАТИСТИЧНИЙ ОПИС ДАНИХ")
print("=" * 80)
print(df.describe())

total_all = df[bike_columns].sum().sum()
print("\n" + "=" * 80)
print("4. ЗАГАЛЬНА КІЛЬКІСТЬ ВЕЛОСИПЕДИСТІВ ЗА РІК НА ВСІХ ВЕЛОДОРІЖКАХ")
print("=" * 80)
print(f"Всього велосипедистів: {total_all:,.0f}")

print("\n" + "=" * 80)
print("5. ЗАГАЛЬНА КІЛЬКІСТЬ ВЕЛОСИПЕДИСТІВ НА КОЖНІЙ ВЕЛОДОРІЖЦІ")
print("=" * 80)
bike_totals = df[bike_columns].sum().sort_values(ascending=False)
for col, total in bike_totals.items():
    print(f"{col}: {total:,.0f}")

df['Month'] = df['Date'].dt.month
df['MonthName'] = df['Date'].dt.month_name()

print("\n" + "=" * 80)
print("6. НАЙПОПУЛЯРНІШИЙ МІСЯЦЬ ДЛЯ ТРЬОХ НАЙЗАВАНТАЖЕНІШИХ ВЕЛОДОРІЖОК")
print("=" * 80)

top_3_bikes = bike_totals.head(3).index.tolist()

month_names_uk = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

for bike in top_3_bikes:
    monthly = df.groupby('Month')[bike].sum()
    max_month_num = monthly.idxmax()
    max_count = monthly.max()
    print(f"{bike}: {month_names_uk[max_month_num]} ({max_count:,.0f} велосипедистів)")

print("\n" + "=" * 80)
print(f"7. ГРАФІК ЗАВАНТАЖЕНОСТІ ВЕЛОДОРІЖКИ '{top_3_bikes[0]}' ПО МІСЯЦЯМ")
print("=" * 80)

selected_bike = top_3_bikes[0]
monthly_data = df.groupby('Month')[selected_bike].sum()

plt.rcParams['font.family'] = 'DejaVu Sans'

plt.figure(figsize=(14, 7))
bars = plt.bar(monthly_data.index, monthly_data.values, color='steelblue', 
               edgecolor='navy', linewidth=1.5)

max_idx = monthly_data.idxmax()
bars[max_idx - 1].set_color('crimson')

plt.xlabel('Місяць', fontsize=13, weight='bold')
plt.ylabel('Кількість велосипедистів', fontsize=13, weight='bold')
plt.title(f'Завантаженість велодоріжки {selected_bike} по місяцям (2015 рік)', 
          fontsize=15, weight='bold', pad=20)
plt.xticks(range(1, 13), 
           ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 
            'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру'])
plt.grid(axis='y', alpha=0.3, linestyle='--')

for i, v in enumerate(monthly_data.values):
    plt.text(i + 1, v + max(monthly_data.values) * 0.02, 
             f'{v:,.0f}', ha='center', va='bottom', fontsize=9, weight='bold')

plt.tight_layout()
plt.show()

print("\nГрафік побудовано успішно!")
print("\n" + "=" * 80)
print("ДОДАТКОВА СТАТИСТИКА")
print("=" * 80)
print(f"Середня кількість велосипедистів на день: {df[bike_columns].sum(axis=1).mean():,.0f}")
print(f"Максимальна кількість за день: {df[bike_columns].sum(axis=1).max():,.0f}")
print(f"Мінімальна кількість за день: {df[bike_columns].sum(axis=1).min():,.0f}")