import tkinter
import tkinter.ttk

import wikitools.ui.template_pretty.view as tp_v
import wikitools.ui.template_pretty.model as tp_m
import wikitools.ui.template_pretty.controller as tp_c

import wikitools.ui.book_parse.view as bp_v
import wikitools.ui.book_parse.model as bp_m
import wikitools.ui.book_parse.controller as bp_c


class WikiToolsView:
    __root = None

    tabs = {}

    template_pretty = None
    book_parse = None
    article_parse = None

    def __init__(self):
        self.create_ui()
        self.template_pretty = tp_v.TemplatePrettyView(root=self.__root,
                                                       main_frame=
                                                       self.tabs['template_pretty'])
        self.book_parse = bp_v.BookParseView(root=self.__root,
                                             main_frame=self.tabs['book_parse'])
        #
        # self.article_parse = ap_v.ArticleParseView(root=self.__root,
        #                                 main_frame=self.tabs['article_parse'])

    @property
    def root(self):
        return self.__root

    def create_ui(self):
        self.__root = tkinter.Tk()
        # root = self.__root
        self.__root.title('Wiki Tools')
        w = 600
        h = 500
        self.__root.geometry('%sx%s+0+0' % (w, h))

        notebook = tkinter.ttk.Notebook(self.__root)
        notebook.pack(fill='both', expand=True)

        TABS = (
            ('template_pretty', 'Template Pretty'),
            ('book_parse',      'Book Parse'),
            ('article_parse',   'Article Parse'),
            )

        for name, title in TABS:
            page = tkinter.ttk.Frame(self.__root)

            notebook.add(page, text=title)
            self.tabs[name] = page

    def close(self):
        print('close')
        self.__root.destroy()
        self.__root.quit()


class WikiToolsModel:
    view = None

    template_pretty = None
    book_parse = None
    article_parse = None
    ##

    def __init__(self, view):
        self.view = view
        self.template_pretty = tp_m.TemplatePrettyModel(view.template_pretty)
        self.book_parse = bp_m.BookParseModel(view.book_parse)
        # self.article_parse = ap_m.ArticleParseModel(view.article_parse)


class WikiToolsController:
    view = None
    model = None

    template_pretty = None
    book_parse = None
    article_parse = None

    def __init__(self):
        self.view = WikiToolsView()
        self.model = WikiToolsModel(self.view)

        self.template_pretty = tp_c.TemplatePrettyController(self.view.template_pretty,
                                                             self.model.template_pretty)

        self.book_parse = bp_c.BookParseController(self.view.book_parse,
                                                   self.model.book_parse)
        #
        # self.article_parse = ap_c.IndexatorController(self.view.indexator,
        #                                           self.model.indexator)

        self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
        self.view.root.mainloop()

    def close_handler(self):
        self.view.close()


class WikiToolsApp:
    controller = None

    def __init__(self):
        self.controller = WikiToolsController()
