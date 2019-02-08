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

  # push
  # same as a[len(a):] = [x]
  a = [1, 2, 3, 4]
  a.append(5)
  print(a)

  # concat
  # same as a[len(a):] = iterable
  a.extend([6, 7])
  print(a)

  # insert
  a.insert(3, 9)
  print(a)

  # remove
  a.remove(9)
  print(a)

  # pop
  a.pop()
  a.pop(2)
  print(a)

  # reverse
  a.reverse()
  print(a)

  # index(val, [start], [end])
  # return an index of the matched value.
  ind = a.index(5)
  print(ind)

  # count
  # Return the number of times x appears in the list.
  print(a.count(5))
  a.append(5)
  print(a.count(5))

  # sort(key:func=None, reverse:bool=False)
  a.sort()
  print(a)
  a.sort(key=int.bit_length, reverse=True)
  print(a)

  # shallow copy
  # same as a[:]
  b = a.copy()
  print(b)

  # clear
  # same as del a[:]
  a.clear()
  print(a)

  # nest
  c = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 0]
  ]

  # zip
  print(list(zip(c)))

