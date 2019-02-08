# -*- coding: utf-8 -*-

import sys
import io
import traceback
import json
from pprint import pprint

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
  
  jsonRes = './res/user.json'
  j = json.load(open(jsonRes, 'r', encoding='utf-8'))
  pprint(j[0], width=79)

  print(json.dumps([1, 'simple', 'list']))

  print(json.dumps({'a':1, 'b': 2}))
