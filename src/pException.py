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
    # traceback.print_exc()()
    pass

if __name__ == '__main__':
  std_encoding('utf-8')
  
  try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
  except OSError as err:
    print("OS error: {0}".format(err))
  except ValueError:
    print("Could not convert data to an integer.")
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
  finally:
    pass
