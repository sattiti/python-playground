# -*- coding: utf-8 -*-

import sys
import io
import traceback
import codecs
from pathlib import Path

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
    
    filepath = './res/index.html'
    f        = Path(filepath).open(mode='r', encoding='utf-8')

  for line in f.readlines():
    sys.stdout.buffer.write(codecs.encode(line, 'utf-8'))
    
    # encode, decode
    # errors
    #   strict            Raise UnicodeError (or a subclass); this is the default.
    #   ignore            Ignore the malformed data and continue without further notice.
    #   replace           Replace with a suitable replacement marker U+FFFD '?
    #   xmlcharrefreplace Replace with the appropriate XML character reference.
    #   backslashreplace  Replace with backslashed escape sequences.
    #   namereplace       Replace with \N{...} escape sequences.
    #   surrogateescape   On decoding, replace byte with individual surrogate code ranging from U+DC80 to U+DCFF.
    print(codecs.encode('ああああ', encoding='utf-8', errors='strict'))
    print(codecs.decode(b'aaa', encoding='utf-8', errors='strict'))

    # Return a codecs.CodecInfo object.
    ci = codecs.lookup('utf-8')
    print(ci.name)
    print(codecs.getencoder('utf-8')('aaa'))
    print(codecs.getdecoder('utf-8')(b'aaa'))

    # Return StreamReader, StreamWriter
    # r = codecs.getreader('utf-8')
    # r.read([size[, chars[, firstline]]])
    # r.readline([size[, keepends]])
    # r.readlines([sizehint[, keepends]])
    # r.reset()

    # w = codecs.getwriter('utf-8')
    # w.write(obj)
    # w.writelines(list)
    # w.reset()

    # codecs.open(filename, mode='r', encoding=None, errors='strict', buffering=1)
    # codecs.EncodeFile(file, data_encoding, file_encoding=None, errors='strict')
