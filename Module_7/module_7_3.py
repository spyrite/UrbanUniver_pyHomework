PUNCTUATION_SYMBOLS = [',', '.', '=', '!', '?', ';', ':', ' - ']


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            all_words[file_name] = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for word in line.lower().split():
                        [word.replace(sym, "") for sym in PUNCTUATION_SYMBOLS]
                        all_words[file_name].append(word)
        return all_words

    def find(self, word):
        word_positions = {}
        for file_name in self.file_names:
            word_positions[file_name] = self.all_words[file_name].index(word.lower()) + 1 \
                if word.lower() in self.all_words[file_name] else -1
        return word_positions

    def count(self, word):
        word_counts = {}
        for file_name in self.file_names:
            word_counts[file_name] = self.all_words[file_name].count(word.lower())
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print('---')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
