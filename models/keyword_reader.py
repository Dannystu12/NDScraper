import csv

class KeywordReader:
    def __init__(self, path):
        self.path = path

    def get_keywords(self):
        keywords = []
        with open(self.path, 'r', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue

                if row[0].strip() == '':
                    continue

                keywords.append(row[0].strip())

        return keywords