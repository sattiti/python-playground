# -*- coding: utf-8 -*-

import sys
import io
import traceback
import math

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

  doc = """hello world
ahola
ハローワールド
"""

  print(("%s" % 'hello world.'))
  print(("%s" % 'ハローワールド'))
  print(("%s" % doc))

  # formatted
  s1 = 'abc'
  s2 = 'efg'
  s3 = 'hij'

  print("i can sing my {}".format(s1))
  print('you can sing your {} and {}'.format(s1, s2))

  # add zero to the front of str
  print('2'.zfill(5))
  print('%05d' % 10)
  print('%5.5f' % math.pi)

