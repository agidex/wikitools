from wikitools.ui.book_parse.controller import BookParseController


class BookParseApp:
    controller = None

    def __init__(self):
        self.controller = BookParseController()
