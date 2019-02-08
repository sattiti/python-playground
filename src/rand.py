# -*- coding: utf-8 -*-

import sys
import io
import traceback
import random

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

  times  = 10
  ptlist = [45, 95, 20, 100, 20, 2, 2220, 2938]
  fruits = ['grape', 'apple', 'orange', 'banana', 'lemon']

  # 乱数生成を初期化する。
  # random.seed(a=None, version=2)
  # a: 省略か None の場合、システムの時刻を使う。
  random.seed()

  # 乱数生成器の現在の内部状態を記憶したオブジェクトを返す。
  # print(random.getstate())
  # random.setstate(state)

  for i in range(times):
    # random.getrandbits(k)
    # k 桁の乱数ビットで Python の整数を生成し返す。
    print('getrandbits: {}'.format(random.getrandbits(3)))

    # random.randrange(start, stop[, step])
    print('range:       {}'.format(random.randrange(1, times, step=2)))

    # random.randint(a, b)
    # random.range(a, b+1) のエイリアス
    print('randint:     {}'.format(random.randint(1, times)))

    # random()
    print('rand:        {}'.format(random.random()))

  # random.choice(seq)
  # seq からランダムに要素を返す。
  print('choice: {}\n'.format(random.choice(ptlist)))
