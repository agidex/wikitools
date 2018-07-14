from wikitools.ui.template_pretty.controller import TemplatePrettyController


class TemplatePrettyApp:
    controller = None

    def __init__(self):
        self.controller = TemplatePrettyController()
