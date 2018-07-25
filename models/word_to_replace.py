class WordToReplace:
    def __init__(self, word, replacement, is_bold):
        self.word = word
        self.replacement = replacement
        self.is_bold = is_bold

    def __str__(self):
        return 'word:{}\nreplacement:{}\nis_bold:{}'.format(self.word, self.replacement, self.is_bold)