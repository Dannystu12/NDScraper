import os
from models.keyword_reader import KeywordReader

cwd = os.getcwd()
KEYWORD_PATH = os.path.join(cwd, 'inputs', 'keywords.csv')

keyword_reader = KeywordReader(KEYWORD_PATH)
keywords = keyword_reader.get_keywords()
print(keywords)
