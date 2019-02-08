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
    # traceback.print_exc()()
    pass

if __name__ == '__main__':
  std_encoding('utf-8')

  x = int(input("Please enter an integer: "))

  if x < 0:
    x = 0
    print('Negative changed to zero')
  elif x == 0:
    print('Zero')
    sys.exit(0)
  elif x == 1:
    print('Single')
  else:
    print('More')

