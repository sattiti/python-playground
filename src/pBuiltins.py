# -*- coding: utf-8 -*-

import sys
import io
import traceback
import builtins

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

  # see here for more information.
  # https://docs.python.org/ja/3/library/stdtypes.html

  # print builtlns func
  print('\n'.join(sorted(dir(builtins))))

  # print dir() document.
  print(dir.__doc__)

  # print repr document.
  print(repr.__doc__)

