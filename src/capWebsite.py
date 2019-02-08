# -*- coding: utf-8 -*-

import sys
import io
import traceback
import re
import os
import time
import yaml
from pathlib import Path
import requests
from selenium import webdriver

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

  b      = webdriver.Chrome()
  urls   = yaml.load(Path("./urls.yml").open("r", encoding="utf-8"))
  dist   = "%s/Desktop/images" % Path.home()
  ext    = ".png"
  output = ""
  
  if not Path(dist).exists():
    Path(dist).mkdir()
  
  try:
    for url in urls:
      b.get(url)
      output     = "%s/%s%s" %(dist, url.replace("/", "+").replace(":", "+"), ext)
      pageHeight = b.execute_script('return document.body.clientHeight | document.body.scrollHeight | document.documentElement.scrollHeight | document.documentElement.offsetHeight;')
      b.set_window_size(1200, pageHeight)
      time.sleep(1)
      # Path(output).open("wb").write(b.get_screenshot_as_png())
      b.save_screenshot(output)
  except Exception as e:
    traceback.print_exc()
    pass
  finally:
    b.close()
    b.quit()