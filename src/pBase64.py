# -*- coding: utf-8 -*-

import sys
import io
import traceback
import base64

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

  data    = b'hello world. aloha'
  
  # base64
  b64data = base64.b64encode(data)
  print('b64encode: {}\n'.format(b64data))
  print('b64decode: {}\n'.format(base64.b64decode(b64data)))
  
  # base64 standard
  b64_std_data = base64.standard_b64encode(data)
  print('b64_standard_encode: {}\n'.format(b64_std_data))
  print('b64_standard_decode: {}\n'.format(base64.standard_b64decode(b64_std_data)))
  
  # base64 urlsafe
  b64_urlsafe_data = base64.urlsafe_b64encode(data)
  print('b64_urlsafe_encode: {}\n'.format(b64_urlsafe_data))
  print('b64_urlsafe_decode: {}\n'.format(base64.urlsafe_b64decode(b64_urlsafe_data)))

  # b32
  b32_data = base64.b32encode(data)
  print('b32_encode: {}\n'.format(b32_data))
  print('b32_decode: {}\n'.format(base64.b32decode(b32_data)))

  # b16
  b16_data = base64.b16encode(data)
  print('b16_encode: {}\n'.format(b16_data))
  print('b16_decode: {}\n'.format(base64.b16decode(b16_data)))

  # a85
  # using Ascii85
  # base64.a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)
  # base64.a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\v')
  a85_data = base64.a85encode(data)
  print('a85_encode: {}\n'.format(a85_data))
  print('a85_decode: {}\n'.format(base64.a85decode(a85_data)))
  
  # b85
  # base64.b85encode(b, pad=False)
  # base64.b85decode(b)
  b85_data = base64.b85encode(data)
  print('b85_encode: {}\n'.format(a85_data))
  print('b85_decode: {}\n'.format(base64.b85decode(b85_data)))
  
  # base64.decodebytes(s)
  # base64.decodestring(s)
  print('decodebytes: {}\n'.format(b64_urlsafe_data))
  print('decodestring: {}\n'.format(b64_urlsafe_data))

  # base64.encode(input, output)
  # base64.encodebytes(s)
  # base64.encodestring(s)
