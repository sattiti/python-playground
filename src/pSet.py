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

  # Set
  fruits = {'banana', 'apple', 'orange', 'pear', 'apple', 'lemon', 'orange'}
  print(type(fruits))
  print(fruits)
  print('orange' in fruits)
  print('crabgrass' in fruits)
  [print(o) for o in fruits]

  a = set('hello')
  b = set('aloha')

  # an unquie letters
  print(a)

  # letters in a but not in b
  print(a - b)

  # letters in a or b or both
  print(a | b)

  # letters in both a and b
  print(a & b)

  # letters in a or b but not both
  print(a ^ b)

