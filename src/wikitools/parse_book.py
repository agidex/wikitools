import os
import re
from pprint import pprint

# ================================= #


def parse_book(file_name):
    with open(file_name, encoding='utf-8') as fh:
        in_text = fh.read()

    table_re = re.compile('<table id="metadata_content_table">(.*?)</table>')
    keyval_re = re.compile('<td class="metadata_label">(.*?)</td><td class="metadata_value">(.*?)</td>')

    del_re_lst = list()
    del_re_lst.append(re.compile('<span.*?>'))
    del_re_lst.append(re.compile('</span>'))
    del_re_lst.append(re.compile('<a.*?>'))
    del_re_lst.append(re.compile('</a>'))

    table_find = re.search(table_re, in_text)
    if not table_find:
        print('table not found')
    else:
        table_text = table_find.group()
    ##    print(table_text)
        for del_re in del_re_lst:
            table_text = re.sub(del_re, '', table_text)
        
        pairs_find = re.findall(keyval_re, table_text)
    ##    pprint(pairs_find)
        book_dict = dict()
        for key, val in pairs_find:
            book_dict[key] = val
        book_dict['Название'] = book_dict['Название'].split('<br><i>')[0]

        pages = book_dict.get('Количество страниц')
        if (pages):
            book_dict['Количество страниц'] = pages.split(': ')[1]

        isbn_line = book_dict.get('ISBN')
        if (isbn_line):
            book_dict['ISBN'] = isbn_line.split(', ')[0]

        book_dict['Год'] = book_dict['Издатель'].split(', ')[-1]
        book_dict['Издатель'] = ', '.join(book_dict['Издатель'].split(', ')[:-1])
        del book_dict['Экспорт цитаты']
#        pprint(book_dict)

    tpl_text = '''{{книга
 | автор         = %s
 | часть         =
 | ссылка часть  =
 | заглавие      = %s
 | оригинал      =
 | ссылка        =
 | викитека      =
 | ответственный =
 | издание       = %s
 | место         =
 | издательство  = %s
 | год           = %s
 | том           =
 | страницы      =
 | столбцы       =
 | страниц       = %s
 | серия         =
 | isbn          = %s
 | doi           =
 | тираж         =
 | ref           =
}}'''
    if 'Автор' in book_dict.keys():
        author = book_dict.get('Автор')
    else:
        author = book_dict.get('Авторы')
    
    tpl = tpl_text % (author,
                      book_dict.get('Название'),
                      book_dict.get('Издание:'),
                      book_dict.get('Издатель'),
                      book_dict.get('Год'),
                      book_dict.get('Количество страниц'),
                      book_dict.get('ISBN')
                      )
    return tpl

for filename in os.listdir(os.path.curdir):
    if filename.endswith('html') or filename.endswith('htm'):
        parse_book(filename)
            


    
    
















