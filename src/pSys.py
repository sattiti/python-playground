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
    # # traceback.print_exc()()()
    pass

if __name__ == '__main__':
  std_encoding('utf-8')

  print('{}\n'.format(sys.argv))
  print('{}\n'.format(sys.copyright))
  print('{}\n'.format(sys.executable))
  print('{}\n'.format(sys.flags))
  print('{}\n'.format(sys.getdefaultencoding()))
  print('{}\n'.format(sys.getfilesystemencoding()))
  print('{}\n'.format(sys.getfilesystemencodeerrors()))
  print('{}\n'.format(sys.getrefcount(sys)))
  print('{}\n'.format(sys.getrecursionlimit()))
  print('{}\n'.format(sys.getsizeof(sys)))
  print('{}\n'.format(sys.modules))
  print('{}\n'.format(sys.path))
  print('{}\n'.format(sys.platform))
  print('{}\n'.format(sys.prefix))

