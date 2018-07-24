from bs4 import BeautifulSoup
import re

class ReportBuilder:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate(self, entries, keywords, should_highlight):
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
                head_html = str(entry.heading.text) #"<h2>{}</h2>".format(entry.heading)
                body_html = str(entry.body) #"<p>{}</p>".format(entry.body)
                link_html = "<a href={}>{}</a>".format(entry.link, entry.link.split('=')[-1].strip())
                main_body_html += "<h2>{}</h2>".format(link_html + head_html)
                main_body_html += body_html

            if should_highlight:
                main_body_html = self.highlight_keywords(main_body_html, keywords)

            html = html.format(body=main_body_html)
            soup = BeautifulSoup(html, 'lxml')
            output_file.write(soup.prettify())

    def highlight_keywords(self, html, keywords):
        result = html
        for keyword in keywords:
            result = re.sub(r'\b{}\b'.format(keyword),
                            '<span style="color: red;">{}</span>'.format(keyword), result, flags=re.I)
        return result