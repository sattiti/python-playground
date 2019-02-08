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

  players = [
    {'name': 'john', 'age': 20},
    {'name': 'mary', 'age': 23}
  ]

  print('name' in players[0])
  print(players)

  for player in players:
    for k, v in player.items():
      print(k)
      print(v)

  for i, v in enumerate(players):
    print(i, v)

