import csv
import os
import chardet


HEADER = ['KEYWORD']
cwd = os.getcwd()
encoding = ''

with open(os.path.join(os.path.dirname(cwd), 'inputs', 'keywords.txt'), 'rb') as input_file:
    encoding = chardet.detect(input_file.read())['encoding']

with open(os.path.join(os.path.dirname(cwd), 'inputs', 'keywords.txt'), 'r', encoding=encoding) as input_file:
    reader = csv.reader(input_file)
    with open(os.path.join(os.path.dirname(cwd), 'inputs', 'keywords_test.csv'), 'w', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(HEADER)
        for row in reader:
            for keyword in row:
                writer.writerow([keyword.strip()])


