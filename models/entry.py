class Entry:
    def __init__(self, heading, body, link):
        self.heading = heading
        self.body = body
        self.link = link

    def __str__(self):
        return '{}\n{}\n{}'.format(self.heading, self.body, self.link)
