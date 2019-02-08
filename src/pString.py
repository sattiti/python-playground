# -*- coding: utf-8 -*-

import sys
import io
import traceback
import string
from string import Template

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

  print(string.ascii_letters)
  print(string.ascii_lowercase)
  print(string.ascii_uppercase)
  print(string.printable)
  print(string.punctuation)
  print(string.whitespace)
  print(string.digits)
  print(string.hexdigits)
  print(string.octdigits)
  print(string.capwords(string.ascii_letters))

  # template
  s = Template('$who name is $name.')
  a = s.safe_substitute({'who': 'My', 'name': 'john'})
  b = s.substitute({'who': 'His', 'name': 'Paul'})

  print(a)
  print(b)