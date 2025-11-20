import nltk
from nltk.corpus import gutenberg, stopwords
from collections import Counter
import matplotlib.pyplot as plt

def load_resources():
    nltk.download('gutenberg', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)

def get_top_words(word_list, top_n=10):
    freq = Counter(word_list)
    return freq.most_common(top_n), freq

def plot_top_words(words, frequencies, title, filename):
    plt.figure(figsize=(12, 6))
    plt.bar(words, frequencies)
    plt.xlabel('Слова', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()

def filter_text(words):
    stop_words = set(stopwords.words('english'))
    return [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

def main():
    load_resources()

    print("\nЗавантаження тексту 'Moby Dick'...")
    text = gutenberg.words('melville-moby_dick.txt')
    total_words = len(text)
    print(f"\n1. Загальна кількість слів у тексті: {total_words}")

    print("\n2. 10 найбільш вживаних слів (без обробки):")
    top_raw, raw_freq = get_top_words(text)
    for w, f in top_raw:
        print(f"   '{w}': {f}")

    plot_top_words(
        [w for w, f in top_raw],
        [f for w, f in top_raw],
        "10 найбільш вживаних слів у 'Moby Dick' (без обробки)",
        "moby_dick_top_10_raw_words.png"
    )

    print("\n3. Обробка тексту (видалення стоп-слів та пунктуації)...")
    filtered_words = filter_text(text)
    print(f"   Кількість слів після обробки: {len(filtered_words)}")

    print("\n4. 10 найбільш вживаних слів (після обробки):")
    top_filtered, filtered_freq = get_top_words(filtered_words)
    for w, f in top_filtered:
        print(f"   '{w}': {f}")

    plot_top_words(
        [w for w, f in top_filtered],
        [f for w, f in top_filtered],
        "10 найбільш вживаних слів у 'Moby Dick' (після обробки)",
        "moby_dick_top_10_filtered_words.png"
    )

    print("\n" + "=" * 60)
    print("ПІДСУМКОВА СТАТИСТИКА:")
    print("=" * 60)
    print(f"Загальна кількість слів: {total_words}")
    print(f"Кількість унікальних слів (до обробки): {len(raw_freq)}")
    print(f"Кількість слів після обробки: {len(filtered_words)}")
    print(f"Кількість унікальних слів (після обробки): {len(filtered_freq)}")
    print(f"Видалено слів: {total_words - len(filtered_words)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
