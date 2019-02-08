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

  def scope_test():
    def do_local():
      v = "local"

    def do_nonlocal():
      nonlocal v
      v = "nonlocal"

    def do_global():
      global v
      v = "global"

    v = "test"
    print(v)
    
    # no change
    do_local()
    print(v)
    
    # change to nonlocal
    do_nonlocal()
    print(v)
    
    # nonlocal
    do_global()
    print(v)

  scope_test()
  
  # global
  print(v)
