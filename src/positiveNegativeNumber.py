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
    # traceback.print_exc()
    pass

if __name__ == '__main__':
  std_encoding('utf-8')
  
  num = (
    (5, 7, -2, 6),
    (-4, 3, -8, 6),
    (9, -2, -6, -7),
  )
  
  calMethod = ('+', '-', '*', '/')
  # 負数の絶対値を引く = 正負の数 + 負数
  # 負数の絶対値を足す = 正負の数 - 負数
  # 正数 = 正数 * 正数
  # 正数 = 負数 * 負数
  # 負数 = 正数 * 負数
  # 負数 = 負数 * 正数
  for i, name in enumerate(calMethod):
    print(calMethod[i])
    for n in num:
      if i is 0:
        print('{} = {} + {} + {} + { }'.format(n[0] + n[1] + n[2] + n[3], n[0], n[1], n[2], n[3]))
      elif i is 1:
        print('{} = {} - {} - {} - {}'.format(n[0] - n[1] - n[2] -n[3], n[0], n[1], n[2], n[3]))
      elif i is 2:
        print('{} = {} * {} * {} * {}'.format(n[0] * n[1] * n[2] * n[3], n[0], n[1], n[2], n[3]))
      else:
        print('{} = {} / {} / {} / {}'.format(n[0] / n[1] / n[2] / n[3], n[0], n[1], n[2], n[3]))
    print()
