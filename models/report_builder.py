import re

class ReportBuilder:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate(self, entries, keywords):
        html = """
        <html>
            <head></head>
            <body>
                {}
            </body>
        </html>
        """
        with open(self.output_path, 'w', encoding='utf-16') as output_file:
            main_body_html = ''
            for entry in entries:
                head_html = str(entry.heading.text) #"<h2>{}</h2>".format(entry.heading)
                body_html = str(entry.body) #"<p>{}</p>".format(entry.body)
                link_html = "<div><a href={}>{}</a></div>".format(entry.link, entry.link.split('=')[-1])
                main_body_html += self.highlight_keywords("<h2>{}</h2>".format(head_html), keywords)
                main_body_html += self.highlight_keywords(body_html, keywords)
                main_body_html += link_html

            html = html.format(main_body_html)
            output_file.write(html)

    def highlight_keywords(self, html, keywords):
        result = html
        for keyword in keywords:
             result = re.sub(r'\b{}\b'.format(keyword), '<span style="background-color: papayawhip;">{}</span>'.format(keyword), result, flags=re.I)
        return result