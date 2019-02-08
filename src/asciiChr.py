# -*- coding: utf-8 -*-

import sys
import io
import traceback
import base64

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
  
  a = '※米脱毛あほ@a<>'
  b = []
  for c in a:
    print('char:  {}'.format(c))
    print('ascii: {}'.format(ascii(c)))
    print('ord:   {}'.format(ord(c)))
    print('oct:   {}'.format(oct(ord(c))))
    b.append(ord(c))
  
  print()
  for c in b:
    print('ord: {}'.format(c))
    print('chr: {}'.format(chr(c)))
