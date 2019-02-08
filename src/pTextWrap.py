# -*- coding: utf-8 -*-

import sys
import io
import traceback
import textwrap
from pathlib import Path

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
  
  f = Path('./res/index.html').open('r', encoding='utf-8')
  s = f.read()
  f.close()
  
  # 設定した文字数に到達したら、分割し list にいれる。
  print(textwrap.wrap(s, width=10))
  
  # 設定した横幅ごと改行する。
  print(textwrap.fill(s, width=10))
  
  # 設定した文字数にを越えだ場合、短略して表示される。短略文字は placeholder パラメータを使って変更をすることができる。
  print(textwrap.shorten(s, width=40, placeholder='++++'))
  
  # textwrap.indent(text, prefix, predicate=None)
  c = textwrap.indent(s, '  ')
  print(c)
  
  # 各行共通している先頭の空白部分が削除される
  print(textwrap.dedent(c))
  
  
