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


class CS(object):
  name = 'abc'

  def __init__(self):
    self._age = 20

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, val):
    self._age = val

  @age.deleter
  def age(self):
    del self._age


  @staticmethod
  def static_display():
    print(CS.name)

  @classmethod
  def class_display(cls):
    print(cls.name)

class CCS(CS):
  name = 'def'

class C(object):
  name = 'abc'

  def __init__(self):
    self._age = 10
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, v):
    self._age = v
  
  @age.deleter
  def age(self):
    del self._age
  
  @staticmethod
  def static_display():
    print(C.name)
  
  @classmethod
  def class_display(cls):
    print(cls.name)

class CC(C, CCS):
  name = 'cde'

if __name__ == '__main__':
  std_encoding('utf-8')
  
  c = CS()
  c.age = 30
  print(c.age)
  
  CCS.static_display()
  CCS.class_display()
  
  C.static_display()
  C.class_display()

  # C.name のまま出力する。
  # abc
  CC.static_display()
  
  # 継承先の CC.name を出力する。
  # cde
  CC.class_display()
