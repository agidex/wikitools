from wikitools.tpl_pretty import tpl_pretty2


class TemplatePrettyModel(object):
    view = None

    def __init__(self, view_):
        self.view = view_

    def transmute(self):
        txt = self.view.get_text()
        self.view.add_text(tpl_pretty2(txt))
        print('TRANSMUTE DONE')
