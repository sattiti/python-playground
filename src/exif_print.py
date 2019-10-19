# -*- coding: utf-8 -*-

import sys
import io
import traceback
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import requests

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
  
  img_path = ''
  
  c = requests.get(img_path)
  img = Image.open(io.BytesIO(c.content))
  exif = img._getexif()
  for id, val in exif.items():
    tag = TAGS.get(id, id), val
    print(tag)