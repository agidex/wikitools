from wikitools.ui.template_pretty.view import TemplatePrettyView
from wikitools.ui.template_pretty.model import TemplatePrettyModel


class TemplatePrettyController(object):
    model = None
    view = None

    def __init__(self, view=None, model=None):
        if view is None:
            self.view = TemplatePrettyView()
        else:
            self.view = view
        if model is None:
            self.model = TemplatePrettyModel(self.view)
        else:
            self.model = model

        self.bind_handlers()

        if view is None:
            self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
            self.view.root.mainloop()

    def close_handler(self):
        self.view.close()

    def bind_handlers(self):
        self.view.buttons['transmute'].bind("<Button-1>", self.transmute)
        # binding modified event
        self.view.text['in'].bind("<<Modified>>", self.transmute)

    def transmute(self, event):
        self.model.transmute()



