import tkinter
import tkinter.ttk

from wikitools.ui.common import mk_treeview, PageView, mk_scrollable_area


class TemplatePrettyView(PageView):

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
            'title': 'Template Pretty',
        }
        return param

    def make_widgets(self, main_frame):
        left_frame = tkinter.Frame(main_frame, bg='red', bd=self.bd)
        left_frame.pack(side='left', fill='both', expand=True)

        in_frame = tkinter.Frame(left_frame, bg='green', bd=self.bd)
        in_frame.pack(side='top', fill='both', expand=True)

        self.text['in'] = tkinter.Text(in_frame, width=5)
        self.text['in'].pack(side='left', fill='x', expand=True)

        mk_scrollable_area(self.text['in'], in_frame, 'y')

        self.buttons['transmute'] = tkinter.ttk.Button(left_frame, text='Transmute')
        self.buttons['transmute'].pack(side='bottom', fill='x', expand=False)

        out_frame = tkinter.Frame(main_frame, bg='blue', bd=self.bd)
        out_frame.pack(side='left', fill='both', expand=True)

        self.text['out'] = tkinter.Text(out_frame, width=5)
        self.text['out'].pack(side='left', fill='y', expand=True)

        mk_scrollable_area(self.text['out'], out_frame, 'y')

    def get_text(self):
        return self.text['in'].get(1.0, tkinter.END)

    def add_text(self, text):
        self.text['out'].insert(tkinter.END, text)
