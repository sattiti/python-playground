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

  words = ['cat', 'window', 'defenestrate']

  for w in words:
    print(w, len(w))


  for w in words[:]:
    print(w)


  # range
  for i in range(0, 30, 3):
    print(i)


  # break
  for n in range(2, 10):
    for x in range(2, n):
      if n % x == 0:
        print(n, 'equals', x, '*', n//x)
        break
    else:
      print(n, 'is a prime number')


  # continue
  for num in range(2, 10):
    if num % 2 == 0:
      print("Found an even number", num)
      continue
    print("Found a number", num)


  # while
  # Fibonacci
  def fib(n):
    a, b = 0, 1
    while a < n:
      print(a, end=' ')
      a, b = b, a+b
      print()
  fib(19)

