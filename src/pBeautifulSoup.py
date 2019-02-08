# -*- coding: utf-8 -*-

import sys
import io
import traceback
import re
from bs4 import BeautifulSoup

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

  html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title></title>
</head>
<body>
<div class="wrapper">
<header id="header">
<h1 id="logo">LOGO</h1>
<nav>
<ul id="hnav">
<li class="hn" id="hn0"><a href="/">HOME</a></li>
<li class="hn" id="hn1"><a href="/about/">About</a></li>
<li class="hn" id="hn2"><a href="/works/">Works</a></li>
<li class="hn" id="hn3"><a href="/contact/">Contact</a></li>
</ul>
</nav>
</header>
</div>
<div class="wrapper">
<main id="contents">
<h2>main page</h2>
<p>hello</p>
<div class="tb0">
<table>
<tr>
<th><div><p>name</p></div></th>
<th>value</th>
</tr>
<tr>
<td><div><p>aaa</p></div></td>
<td>bbb</td>
</tr>
</table>
</div>
</main>
</div>
<div class="wrapper">
<footer id="footer">
<nav>
<ul id="fnav">
<li class="fn" id="fn0"><a href="/">HOME</a></li>
<li class="fn" id="fn1"><a href="/about/">About</a></li>
<li class="fn" id="fn2"><a href="/works/">Works</a></li>
<li class="fn" id="fn3"><a href="/contact/">Contact</a></li>
</ul>
</nav>
</footer>
</div>
</body>
</html>
"""
  try:
    doc = BeautifulSoup(html, 'html.parser')

    # css select
    for tag in doc.select('table > tr > td > div'):
      v = tag.string
      tag.replace_with(v)
      tag.wrap(doc.new_tag('span'))

    # unwrap tag
    doc.table.tr.th.div.unwrap()

    # find_all
    for tag in doc.find_all("li", text=re.compile("hn([0-9]+)?")):
      del tag['class']
      print(tag)

    # find the first element
    # return None if tag not exists
    print(doc.find('a'))
    print(doc.a)

    # get attr
    print(doc.a.get('href'))

    # get string
    print(doc.a.string)

    print(doc)
  except Exception as e:
    # traceback.print_exc()()
    sys.exit()

