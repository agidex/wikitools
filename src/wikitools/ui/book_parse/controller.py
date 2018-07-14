from wikitools.ui.book_parse.view import BookParseView
from wikitools.ui.book_parse.model import BookParseModel


class BookParseController(object):
    model = None
    view = None

    def __init__(self, view=None, model=None):
        if view is None:
            self.view = BookParseView()
        else:
            self.view = view
        if model is None:
            self.model = BookParseModel(self.view)
        else:
            self.model = model

        self.bind_handlers()

        if view is None:
            self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
            self.view.root.mainloop()

    def close_handler(self):
        self.view.close()

    def bind_handlers(self):
        self.view.buttons['parse'].bind("<Button-1>", self.parse)

    def parse(self, event):
        self.model.parse()



