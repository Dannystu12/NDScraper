from bs4 import BeautifulSoup
import re

class ReportBuilder:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate(self, entries, keywords, words_to_replace, should_highlight):
        html = """
        <html>
            <head>
                <style>
                    body {{font-family: "Calibri"; font-size: 11pt;}}
                    h2   {{font-weight: bold; font-size: 11pt;}}
                </style>
            </head>
            <body>
                {body}
            </body>
        </html>
        """
        with open(self.output_path, 'w', encoding='utf-16') as output_file:
            main_body_html = ''
            for entry in entries:
                entry_html = '<div class="entry">{}</div>'
                head_html = entry.heading
                body_html = "<p>{}</p>".format(entry.body)
                link_html = "<a href={}>{}</a>".format(entry.link, entry.link.split('=')[-1].strip())
                entry_html = entry_html.format("<h2>{}</h2>".format(link_html + head_html) + body_html)
                main_body_html += entry_html

            if should_highlight:
                main_body_html = self.highlight_keywords(main_body_html, keywords)

            main_body_html = self.replace_words(main_body_html, words_to_replace)
            html = html.format(body=main_body_html)
            soup = BeautifulSoup(html, 'lxml')

            output_file.write(re.sub('(<br/>\s+){3,}', '<br/><br/>', soup.prettify(formatter=None)))

    def highlight_keywords(self, html, keywords):
        result = html
        for keyword in keywords:
            result = re.sub(r'\b({})\b'.format(keyword),
                            '<span style="color: red;">{}</span>'.format(r'\1'), result, flags=re.I)
        return result

    def replace_words(self, html, words_to_replace):
        result = html
        for word_to_replace in words_to_replace:
            replacement = word_to_replace.replacement
            if word_to_replace.is_bold:
                replacement = "<strong>{}</strong>".format(replacement)
            result = re.sub(r'{}'.format(word_to_replace.word), replacement, result, flags=re.I)
        return result