# -*- coding: utf-8 -*-

import sys
import io
import traceback
import math

def std_encoding(charset):
  try:
    sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding=charset)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=charset)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=charset)
  except Exception as e:
    # traceback.print_exc()()
    pass

def puts_type_val(v):
  print(type(v), v)

if __name__ == '__main__':
  std_encoding('utf-8')

  # Literal
  # rf'' raw formatted string
  # rb'' raw binary

  # b'' binary
  puts_type_val(b'aaa')

  # r'' raw string
  puts_type_val(r'john')

  # u'' unicode
  puts_type_val(u'helloworld')

  # f'' formatted string
  # v3.6 above
  name = r'peter'
  print(f'My name is {name}')

  # Numeric literal
  print(1_0_001)

  # oct
  print(0o700)

  # hex
  print(0xfa)

  # exponentfloat
  print(2e1)

  # None
  puts_type_val(None)

  # bool
  puts_type_val(True)
  puts_type_val(False)

  # int
  puts_type_val(10)

  # float
  puts_type_val(math.pi)

  # immutable sequence
  # str()
  puts_type_val('abcdefg')

  # tuple()
  puts_type_val((1, 2, 3, 4, 5))

  # bytes()
  puts_type_val(b'z')

  # mutable sequence
  # list
  puts_type_val([1, 2, 3, 4])

  # bytearray()
  puts_type_val(bytearray(b'abcdesf'))

  # dict
  puts_type_val({'a': 1, 'b': 2})

  # callable type
  # 関数のドキュメンテーション文字列。
  # ドキュメンテーションがない場合は None。
  # サブクラスに継承されない。
  puts_type_val(__doc__)

  # 関数の名前。
  puts_type_val(__name__)

  # 関数の qualified name
  # puts_type_val(__qualname__)

  # 関数が定義されているモジュールの名前。
  # モジュール名がない場合は None
  # puts_type_val(__module__)

  # デフォルト値を持つ引数に対するデフォルト値が収められたタプル。
  # デフォルト値を持つ引数がない場合には None
  # puts_type_val(__defaults__)

  # コンパイルされた関数本体を表現するコードオブジェクト。
  # puts_type_val(__code__)

  # 関数のグローバル変数の入った辞書。
  # puts_type_val(__globals__)

  # 任意の関数属性をサポートするための名前空間が収められている。
  # puts_type_val(__dict__)

  # None or a tuple of cells that contain bindings for the function's free variables.
  # puts_type_val(__closure__)

  # パラメータの注釈が入った辞書。
  # 辞書のキーはパラメータ名で、返り値の注釈がある場合は、'return' がそのキーとなる。
  # puts_type_val(__annotations__)

  # キーワード専用パラメータのデフォルト値を含む辞書。
  # puts_type_val(__kwdefaults__)

