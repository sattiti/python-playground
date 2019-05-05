# -*- coding: utf-8 -*-

import sys
import io
import traceback
import random
import math

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
  
  def search_num(ary, n):
    size = math.floor(len(ary) *.5)
    print("find num: {}".format(n))
    print("List:     {}\n".format(ary))
    
    l = []
    
    if n == ary[size]:
      print("%d == %d" % (n, ary[size]))
      print("done")
    elif n < ary[size]:
      l = ary[0:size]
      search_num(l, n)
    else:
      l = ary[size:len(ary)]
      search_num(l, n)
  
  
  numAry = list(range(999))
  random.shuffle(numAry)
  
  num = numAry[0]
  random.shuffle(numAry)
  numAry.sort()
  search_num(numAry, num)