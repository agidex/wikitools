# -*- coding: utf-8 -*-

from pathlib import Path
import os

from wikitools.parse_book import parse_book, BookParser

SAVE_PATH = 'Downloads'
ENDS_HTML = 'Google Книги.html'


class BookParseModel(object):
    view = None

    book_parser = None

    def __init__(self, view_):
        self.view = view_

        self.book_parser = BookParser()

    def __readdir(self):
        html_files_path = os.path.join(str(Path.home()), SAVE_PATH)
        for file_name in os.listdir(html_files_path):
            if file_name.endswith(ENDS_HTML):
                txt = parse_book(os.path.join(html_files_path, file_name))
                self.view.add_text(txt)
                self.view.add_text('\n')

    def read_books(self):
        self.book_parser.read_books()
        self.view.display_list(self.book_parser.book_list())

    def parse_all(self):
        self.view.clear_text()
        self.__readdir()
        print('PARSE DONE')

    def parse_selected(self):
        items = self.view.treeviews['books'].selection()
        for item in items:
            n = int('0x' + str(item)[1:], 0)
            print(n)
