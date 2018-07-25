import os
from models.keyword_reader import KeywordReader
from models.spqm_scraper import SPQMScraper
from models.report_builder import ReportBuilder

cwd = os.getcwd()

KEYWORD_PATH = os.path.join(cwd, 'inputs', 'keywords_test.csv')
DRIVER_PATH = os.path.join(cwd, 'venv', 'chromedriver')
SPQM_OUTPUT_PATH = os.path.join(cwd, 'outputs', 'spqm_output.html')
SPQM_URL = 'http://www.parliament.scot/parliamentarybusiness/28877.aspx?SearchType=Advance&DateChoice=2&SortBy=DateSubmitted&Answers=OnlyQuestionAwaitingAnswer&SearchFor=WrittenQuestions&ResultsPerPage=100'#'http://www.parliament.scot/parliamentarybusiness/28877.aspx?SearchType=Advance&DateChoice=1&SortBy=DateSubmitted&Answers=OnlyQuestionAwaitingAnswer&SearchFor=WrittenQuestions&ResultsPerPage=100'#'http://www.parliament.scot/parliamentarybusiness/28877.aspx?SearchType=Advance&Keyword=alcohol&ExactPhrase=True&DateTo=23/07/2018%2023:59:59&SortBy=DateSubmitted&Answers=All&SearchFor=All&ResultsPerPage=100'
SHOULD_HIGHLIGHT = True

def main():
    keyword_reader = KeywordReader(KEYWORD_PATH)
    keywords = keyword_reader.get_keywords()

    spqm_scraper = SPQMScraper(SPQM_URL, DRIVER_PATH)
    entries = spqm_scraper.scrape()

    report_builder = ReportBuilder(SPQM_OUTPUT_PATH)
    report_builder.generate(entries, keywords, SHOULD_HIGHLIGHT)

if __name__ == '__main__':
    main()