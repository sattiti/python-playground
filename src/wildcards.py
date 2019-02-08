# -*- coding: utf-8 -*-

import sys
import io
import traceback
import fnmatch
from pathlib import Path
import os
import re

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
  
  # pattern
  # *      すべてにマッチ。
  # ?      任意の一文字にマッチ。
  # [seq]  seq にある任意の文字にマッチ。
  # [!seq] seq にない任意の文字にマッチ。
  
  for f in os.listdir('.'):
    print(f)
    
  for f in Path('.').rglob('*'):
    # Test weather filename matches pattern.
    print(fnmatch.fnmatchcase(str(f), '*.html'))
    
    if fnmatch.fnmatch(f, '*.html'):
      print(f)
    
  # filter
  print(fnmatch.filter(os.listdir('.'), '*.py'))
  
  # re pattern 変換
  print(fnmatch.translate('*.{html,xml}'))
