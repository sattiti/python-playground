# -*- coding: utf-8 -*-

import sys
import io
import traceback

def std_encoding(charset):
    try:
        # sys.stdin  = codecs.getreader(sys.stdin.encoding)(sys.stdin)
        # sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
        sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding=charset)
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=charset)
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=charset)
    except Exception as e:
        # traceback.print_exc()
        pass

if __name__ == '__main__':
    std_encoding('utf-8')
    a = 'abcdefghijklmnopqrstuvwxyz289020891-^\^0-o[@{}*;:]b}]'
    b = 'hello world'
    c = 'aaaa'
    d = 'https://www.abcde.com/?a=1&b=2&c=3'

    # ab
    print(a[0:2])

    # change the first letter to uppercase
    print(b.capitalize())

    # to uppercase
    print(b.upper())

    # to lowercase
    print(b.upper().lower())

    # casefold
    # 大文字小文字関係なくすべて小文字に変換される。
    print(c.casefold())

    # swapcase
    # 大文字小文字入替
    print(c.swapcase())

    # center, ljust, rjust
    print(c.center(16, '+'))
    print(c.ljust(16, '+'))
    print(c.rjust(16, '+'))

    # count(sub, [start], [end])
    print(a.count('9'))

    # encode(encoding='utf-8', errors='strict')
    # errors: ignore
    #         replace
    #         xmlcharrefreplace
    #         backslashreplace
    print('ハローワールド'.encode('utf-8'))

    # startswith(prefix, [start], [end])
    # endswith(suffix, [start], [end])
    # 文字検索
    print(b.startswith('world'))
    print(b.startswith('h'))

    # expandtabs
    # replace tab to space.
    print("h\te\tl\tl\to".expandtabs(2))

    # find(sub[, start[, end]]))
    # rfind
    # return an index of the matched letter.
    print(a.find('abc'))
    print(a.find('89'))
    print(a.rfind('89'))

    # format
    print('{0} {1}'.format('hello', 'earth'))

    # index
    # rindex
    # return an index of the matched letter.
    # ltr
    print(a.index('8'))

    # rtl
    print(a.rindex('8'))

    # isalnum
    # isalpha
    # isascii
    # isdecimal
    # isdigit
    # isidentifier
    # islower
    # isnumeric
    # isprintable
    # isspace
    # istitle
    # isupper
    print(a.isupper())

    # lstrip
    # rstrip
    # strip([char])
    # 先頭と尾部の char を削除。
    print(b.strip('hdl'))
    print(b.center(20, ' ').lstrip())
    print(b.center(20, ' ').rstrip())

    # partition(sep)
    # rpartition(sep)
    # 分割する
    print(b.center(30, '+').partition('+'))
    print(b.center(30, '+').rpartition('+'))

    # replace(old, new, [count])
    print(b.replace('l', 'L', 1))

    # split
    # rsplit
    print(d.partition('?')[2].split('&'))
    print(d.split('?'))
    print(d.rsplit('?'))

    # splitlines
    # Return a list of the lines in the string, breaking at line boundaries.
    # \n
    # \r
    # \r\n
    # \v | \x0b
    # \f | \x0c
    # \x1c
    # \x1d
    # \x1e
    # \x85
    # \u2028
    # \u2029
    print(d.center(40, '\n').splitlines())

    # title
    # 単語ごとに大文字
    print(b.title())

    # maketrans
    # translate
    # 指定した文字を変換する。
    table = str.maketrans({
        'a': 'あ',
        '9': 'し',
        'c': 'か',
    })
    print(table)
    print(a)
    print(a.translate(table))

    # zfill
    # add zero to the front of str.
    print('10'.zfill(10))

    # join
    print('\n'.join(dir(str())))
