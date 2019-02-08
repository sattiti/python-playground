# -*- coding: utf-8 -*-

import sys
import io
import traceback
import yaml
from pathlib import Path

def std_encoding(charset):
  try:
    # sys.stdin  = codecs.getreader(sys.stdin.encoding)(sys.stdin)
    # sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
    sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding=charset)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=charset)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=charset)
  except Exception as e:
    # traceback.print_exc()()
    print(sys.exc_info())
    pass

if __name__ == '__main__':
  std_encoding('utf-8')

  try:
    yamlRes = './res/a.yaml'
    yml = yaml.load(Path(yamlRes).open(mode='r', encoding='utf-8'))
    print(sys.stdout.buffer.write(yml['cpn'][0]['title'].encode('utf-8')))
  except Exception as e:
    # traceback.print_exc()()
    print(sys.exc_info())
    pass

