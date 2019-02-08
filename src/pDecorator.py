# -*- coding: utf-8 -*-

import sys
import io
import traceback
import functools

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

  def decofunc(tag):
    def inner(f):
      @functools.wraps(f)
      def wrapper(*args, **kwargs):
        # inside program
        print("*args:")
        print("  type: %s" % type(args))
        print("  len: %d" % len(args))

        print("\ndecoratorParams: %s\n" % tag)
        print("**kwargs:")
        print("  type: %s" % type(kwargs))
        print("  len: %d" % len(kwargs))

        # outside program
        f(*args, **kwargs)

      return wrapper
    return inner

  @decofunc('html')
  def a():
    print("a")

  a()

