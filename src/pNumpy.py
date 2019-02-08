# -*- coding: utf-8 -*-

import sys
import io
import traceback
import numpy as np

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
  
  a = np.asarray([[1, 2, 3], [4, 5, 6]])
  print(a.shape)
  
  # random
  r = np.random.rand(10)
  print('random_ary: {}\n'.format(r))
  print('min: {}\n'.format(np.min(r)))
  print('max: {}\n'.format(np.max(r)))
  print('std: {}\n'.format(np.std(r)))
  print('sum: {}\n'.format(np.sum(r)))
