import tkinter
import tkinter.ttk

from wikitools.ui.common import mk_treeview, PageView, mk_scrollable_area


class BookParseView(PageView):

    listboxes = {}
    buttons = {}

    treeviews = {}
    textlabels = {}

    text = {}

    def __init__(self, root=None, main_frame=None):
        super().__init__(root, main_frame)

    def params(self):
        param = {
            'x': 0,
            'y': 0,
            'w': 650,
            'h': 500,
            'title': 'Book Parse',
        }
        return param

    def make_widgets(self, main_frame):
        self.buttons['parse'] = tkinter.ttk.Button(main_frame, text='Parse Book')
        self.buttons['parse'].pack(side='top', fill='x', expand=False)

        out_frame = tkinter.Frame(main_frame, bg='blue', bd=self.bd)
        out_frame.pack(side='bottom', fill='both', expand=True)

        self.text['out'] = tkinter.Text(out_frame, width=5)
        self.text['out'].pack(side='left', fill='y', expand=True)

        mk_scrollable_area(self.text['out'], out_frame, 'y')

    def add_text(self, text):
        self.text['out'].insert(tkinter.END, text)
