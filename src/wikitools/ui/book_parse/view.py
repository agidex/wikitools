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
        path_frame = tkinter.Frame(main_frame, bg='blue', bd=self.bd)
        path_frame.pack(side='top', fill='both', expand=True)

        path_label = tkinter.Label(path_frame, text='Books Path:')
        path_label.pack(side='left', fill='both', expand=False)

        books_path_entry = tkinter.Entry(path_frame)
        books_path_entry.pack(side='left', fill='both', expand=True)

        self.buttons['read'] = tkinter.ttk.Button(path_frame, text='Read Books')
        self.buttons['read'].pack(side='left', fill='x', expand=False)

        table_frame = tkinter.Frame(main_frame, bg='red', bd=self.bd)
        table_frame.pack(side='top', fill='both', expand=True)

        self.treeviews['books'] = mk_treeview(table_frame)

        COLUMNS = (
            ('author', 'Author', 150),
            ('book', 'Book', 200),
            ('year', 'Year', 10),
            ('pages', 'Pages', 15),
            ('isbn', 'ISBN', 70),
        )

        self.treeviews['books']['columns'] = [col[0] for col in COLUMNS]
        for col_id, col_name, col_width in COLUMNS:
            self.treeviews['books'].heading(col_id, text=col_name)
            self.treeviews['books'].column(col_id, width=col_width)

        self.treeviews['books']['show'] = 'headings'

        command_frame = tkinter.Frame(main_frame, bg='yellow', bd=self.bd)
        command_frame.pack(side='top', fill='both', expand=False)

        self.buttons['parse_sel'] = tkinter.ttk.Button(command_frame, text='Parse Selected')
        self.buttons['parse_sel'].pack(side='left', fill='x', expand=False)

        self.buttons['parse_all'] = tkinter.ttk.Button(command_frame, text='Parse All')
        self.buttons['parse_all'].pack(side='left', fill='x', expand=False)

        output_frame = tkinter.Frame(main_frame, bg='blue', bd=self.bd)
        output_frame.pack(side='top', fill='both', expand=True)

        self.text['out'] = tkinter.Text(output_frame, width=5)
        self.text['out'].pack(side='left', fill='y', expand=True)

        mk_scrollable_area(self.text['out'], output_frame, 'y')

    def display_list(self, lst):
        for i in self.treeviews['books'].get_children():
            self.treeviews['books'].delete(i)
        for item in lst:
            item_values = (
                item.get('Автор'),
                item.get('Название'),
                item.get('Год'),
                item.get('Количество страниц'),
                item.get('ISBN'),
            )
            self.treeviews['books'].insert('', 'end', text="", values=item_values)

    def add_text(self, text):
        self.text['out'].insert(tkinter.END, text)

    def clear_text(self):
        self.text['out'].delete('1.0', tkinter.END)
