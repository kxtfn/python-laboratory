import json
import matplotlib.pyplot as plt

with open('rist.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

names = [person['name'] for person in data]
heights = [person['height'] for person in data]

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=names, autopct='%1.1f%%')
plt.title('Розподіл зросту у вибірці')
plt.show()
