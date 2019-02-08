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

  # func 任意長引数
  # * args tuple type
  def sum2(*args):
    print("val: ", args)
    print(("type: %s" % type(args)))
    print(("len: %d" % len(args)))
    return sum(args)

  print(sum2(1, 2, 3, 4))
  print(sum2(1, 2, 3, 4, 5, 6, 7, 8))

  # **kwargs dict type
  def mutable_dict(**kwargs):
    print('val: ', kwargs)
    print(('type: %s' % type(kwargs)))
    print(('len: %d' % len(kwargs)))

  mutable_dict(k1=1, k2=2)
  mutable_dict(name='john', age=20, mail='john@john.john')

  # default argument
  def say(msg1='hello', msg2='world'):
    print(msg1)
    print(msg2)

  say()
  say(msg2='earth')

  # function annotations
  # type hint
  def greeting(name:str) -> str:
    return ('hello %s' % name)

  print(greeting(name='paul'))

