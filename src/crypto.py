# -*- coding: utf-8 -*-

import sys
import io
import traceback
import hashlib
import os

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
  
  sha256 = hashlib.sha256()
  sha256.update(os.urandom(10))
  
  # byte
  print('digest: {}\n'.format(sha256.digest()))
  
  # str
  print('sha256: {}\n'.format(sha256.hexdigest()))
  
  # name
  print('hashname: {}\n'.format(sha256.name))
  
  # size
  print('digest_size: {}\n'.format(sha256.digest_size))
