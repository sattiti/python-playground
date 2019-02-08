# -*- coding: utf-8 -*-

import sys
import io
import traceback
from distutils import sysconfig
import site

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
  
  print(f'userbase: %s\n' % site.getuserbase())
  
  # site-packages
  for a in site.getsitepackages():
    print(a)
  print('site-packages: %s\n' % sysconfig.get_python_lib())
  
  # userpackage
  print('userpackage: %s\n' % site.getusersitepackages())
  
  # config var
  for k, v in sysconfig.get_config_vars().items():
    print('%s: %s' % (k, v))
  
  # makefile
  print('makefile: %s\n' % sysconfig.get_makefile_filename())
  
  # py version
  print('version: %s\n' % sysconfig.get_python_version())