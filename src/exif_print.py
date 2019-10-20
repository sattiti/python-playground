# -*- coding: utf-8 -*-

import sys
import io
import traceback
import codecs
import PIL.Image
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import requests
import photos

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


def print_exif(exif):
  for k, v in exif.items():
    print("{}: {}".format(TAGS.get(k), v))


def get_exif_from_photos():
  a = photos.pick_asset()
  return a.get_image()._getexif()


def get_exif_from_url(img_url):
  c = requests.get(img_url)
  img = Image.open(io.BytesIO(c.content))
  return img._getexif()


if __name__ == '__main__':
  std_encoding('utf-8')
  try:
    img = get_exif_from_photos()
    print_exif(img)
  except Exception as e:
    traceback.print_exc()()
  
  # img_url = ''