from bs4 import BeautifulSoup
from selenium import webdriver
from models.entry import Entry
import re

class SPQMScraper:
    def __init__(self, url, driver_path):
        self.url = url
        self.driver_path = driver_path
        self.entry_link = 'http://www.parliament.scot/parliamentarybusiness/28877.aspx?SearchType=Advance&ReferenceNumbers={}'

    def scrape(self):
        results = []
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        results = self.parse_entries(soup)
        driver.close()
        return results

    def parse_entries(self, soup):
        results = []
        entries = soup.find_all(id=re.compile('MAQA_Search_gvResults_ctl00__\d+'))
        for i, entry in enumerate(entries):
            heading = entry.find('a')
            body = entry.find(id=re.compile('MAQA_Search_gvResults_ctl00_ctl\d+_pnl(Motion|Question)(?<!Header)$'))
            if body == None:
                continue
            paras = body.find_all('p')
            body = ''
            for para in paras:
                body += para.text + '<br><br>'

            link = self.entry_link.format(re.search('\w{3}-\w{5}', heading.text).group())
            entry_obj = Entry(heading.text, body, link)
            results.append(entry_obj)
        return results

