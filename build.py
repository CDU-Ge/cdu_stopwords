# encoding: utf-8
import os


def load_words(directory, encoding='utf-8'):
    words = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if not os.path.isfile(filepath):
            continue
        if not filename.endswith('.txt'):
            continue
        with open(filepath, 'r', encoding=encoding) as file:
            words.extend(file.read().splitlines())
    return words


def main():
    words: list = load_words('stopwords')
    words = list(set(map(lambda w: w.strip(), words)))
    words.sort()
    with open('stopwords.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(words))
    print('stopwords.txt created')
    print('Total words:', len(words))


if __name__ == '__main__':
    main()
