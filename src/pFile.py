# -*- coding: utf-8 -*-

import sys
import io
import traceback
import os
import codecs

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

  # read file
  filepath = 'res/index.html'
  f = open(filepath, 'rb')

  # read one line
  print(f.readline())

  # read each line
  for line in f.readlines():
    print(codecs.decode(line))
  f.close()

  # readall
  with open('index.html', 'rb') as f2:
    print(codecs.decode(f2.read()))
  f2.close()

  # write file
  f = open('res/index2.html', 'a+')
  f.write('hello')

  # goto the 3rd byte.
  f.seek(3)

  print(f.read())
  f.close()

