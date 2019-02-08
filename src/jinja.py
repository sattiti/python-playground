# -*- coding: utf-8 -*-

import sys
import io
import traceback
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

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
  
  base    = Path(__file__).parent
  tplfile = 'res/jinja/a.html.tpl'
  outfile = base.joinpath('out/a.html')
  
  env  = Environment(
    loader = FileSystemLoader(str(base), encoding='utf-8')
  )
  
  tpl  = env.get_template(tplfile)
  html = tpl.render({'h1': 'hello world'})
  Path(outfile).open('w+', encoding='utf-8').write(html.strip())