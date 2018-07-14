import re


def tpl_pretty2(text):
    oneline = ''.join(text.splitlines())

    lines = oneline.split('|')
   # print(lines)

    keyval = []
    max_key_len = 0
    for line in lines:
        if len(line) > 1:
#            print(line)
#            print()
            
#            key, val = line.split('=')
            line_items = line.split('=')
            print(line_items)
            if len(line_items) > 1:
                key = line_items.pop(0).strip()
                # check multiple '='
                if len(line_items) > 1:
                    val = '='.join(line_items).strip()
                else:
                    val = line_items.pop(0).strip()
                    
                if len(key) > max_key_len:
                    max_key_len = len(key)
                keyval.append([key.strip(), val.strip()])

    txt = []
    for key, val in keyval:
        key = key.ljust(max_key_len)
        txt.append('|%s = %s' % (key, val))

    return '\n'.join(txt)


def tpl_pretty(text):
    regex = re.compile('[|].*?(=).*?')

    positions = []
    
    lines = text.split('\n')
    for line in lines:
        m = regex.match(line)
        if m:
            pos = m.span()[1] - 1
            positions.append(pos)
    maxpos = max(positions)
    
    for i, line in enumerate(lines):
        m = regex.match(line)
        if m:
            pos = m.span()[1] - 1
            count = maxpos - pos
            spacer = ''.join([' ' for i in range(count + 1)])
            lines[i] = line.replace('=', spacer + '=')

    return '\n'.join(lines)


def from_file():
    with open('in.txt', encoding='utf-8', errors='replace') as fh:
        text = fh.read()
        print(text)
    text2 = tpl_pretty2(text)
    with open('out.txt', 'w', encoding='utf-8') as fh:
        fh.write(text2)


def from_str():
    s = '''|title='Hamilton' wins 11 Tony Awards on a night that balances sympathy with perseverance|url=http://www.latimes.com/entertainment/arts/culture/la-et-cm-tony-awards-live-updates-20160612-htmlstory.html|work=Los Angeles Times|id=0458-3035|accessdate=2016-08-06|language=en-US
'''
    print(tpl_pretty2(s))


if __name__ == '__main__':
    # from_str()
    from_file()













