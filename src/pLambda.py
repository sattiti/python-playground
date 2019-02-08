# -*- coding: utf-8 -*-

import sys
import io
import traceback
from functools import reduce

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

  # lambda arguments: expression
  def a(n):
    return lambda x: x + n

  print(a(10)(2))

  # map
  fruits = ['apple', 'banana', 'grape', 'lemon', 'melon']

  # lowercase to uppercase
  a = map(lambda x: x[:].upper(), fruits)

  print(list(a))

  # filter
  # return the value if it is True
  b = filter(lambda x: len(x)>5, fruits)
  print(list(b))

  # reduce(func, list)
  # to reduce the sequence to a single value.
  # c = 1 +2 +3 +4 +5
  c = reduce(lambda x, y: x + y, range(1, 5))
  print(c)

