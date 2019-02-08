# -*- coding: utf-8 -*-

import sys
import io
import traceback
import tempfile
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
  
  # tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
  t1 = tempfile.TemporaryFile()
  t1.write(b'hello world')
  t1.seek(0)
  print(t1.read())
  print('name: %s\n' % t1.name)
  t1.close()
  
  # 名前付き tmogile
  # delete が真の場合、ファイルは閉じられたら即座に削除される。
  # tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)
  t2 = tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8')
  t2.write('こんにちは。今日もいい天気です。')
  t2.seek(0)
  print(t2.read())
  print('%s\n' % t2.name)
  t2.close()
  
  # ファイルサイズが max_size を超えるかファイルの fileno() メソッドが呼ばれるまで、データがメモリにスプールされる特徴。
  # tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
  
  # 一時的にディレクトリを生成する。tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)
  t3 = tempfile.TemporaryDirectory()
  print('t3 is dir. {}\n'.format(Path(t3.name).is_dir()))
  print('t3 is file. {}\n'.format(Path(t3.name).is_file()))
  print('%s\n' % t3.name)
  
  # tmp dirname
  print('dirname: {}\n'.format(tempfile.gettempdir()))
  
  # tmp dirname byte ver.
  print('dirname byte ver.: {}\n'.format(tempfile.gettempdirb()))
  
  # dirname prefix
  print('prefix: {}\n'.format(tempfile.gettempprefix()))
  print('prefix byte ver.: {}\n'.format(tempfile.gettempprefixb()))
  
  # get, set tmpdir
  print('tmpdir: {}\n'.format(tempfile.tempdir))
