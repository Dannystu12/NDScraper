import csv
from models.word_to_replace import WordToReplace

class WordsToReplaceReader:
    def __init__(self, path):
        self.path = path

    def get_words_to_replace(self):
        words_to_replace = []
        with open(self.path, 'r', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue

                if row[0].strip() == '':
                    continue

                is_bold = False
                if row[2].strip().lower() == 'true':
                    is_bold = True

                word_to_replace = WordToReplace(row[0], row[1], is_bold)
                words_to_replace.append(word_to_replace)

        return words_to_replace