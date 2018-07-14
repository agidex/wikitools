# -*- coding: utf-8 -*-

from pathlib import Path
import os

from wikitools.parse_book import parse_book

SAVE_PATH = 'Downloads'
ENDS_HTML = 'Google Книги.html'


class BookParseModel(object):
    view = None

    def __init__(self, view_):
        self.view = view_

    def __readdir(self):
        html_files_path = os.path.join(str(Path.home()), SAVE_PATH)
        for file_name in os.listdir(html_files_path):
            if file_name.endswith(ENDS_HTML):
                txt = parse_book(os.path.join(html_files_path, file_name))
                self.view.add_text(txt)
                self.view.add_text('\n')

    def parse(self):
        self.__readdir()
        print('PARSE DONE')
