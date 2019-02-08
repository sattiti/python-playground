# -*- coding: utf-8 -*-

import sys
import io
import traceback

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

  # Using io.stringIO to read strings as same as reading a file.
  # io.stringIO(initial_value='', newline='\n')
  a = io.StringIO("""あい、ハロー。駅駅
acbdefg
志大才疎
  """)
  print(a.readlines())
  a.close()
  
  # str
  # sys.stdin.read(str)
  # sys.stdout.write(str)
  
  # byte
  # sys.stdin.buffer.read(b)
  # sys.stdout.buffer.write(b)
