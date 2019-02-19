# -*- coding: utf-8 -*-

import sys
import io
import traceback
from urllib.parse import urlparse
import pandas as pd

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
    
  queries = urlparse(sys.argv[-1]).query.split("&")
  m = {}
    
  for v in queries:
    q = v.split("=")
    m[q[0]] = q[1]
    
  pd.set_option('display.width', 999)
  pd.set_option('max_coleidth', 999)
  pd.set_option('display.colheader_justify', 'left')
  pd.set_option('display.unicode.east_asian_width', True)
  
  s = pd.Series(m)
  sMax = s.str.len().max()
  print(s.str.ljust(sMax).to_string())
