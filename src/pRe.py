# -*- coding: utf-8 -*-

import sys
import io
import re

def std_encoding(charset):
  # sys.stdin  = codecs.getreader(sys.stdin.encoding)(sys.stdin)
  # sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
  sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding=charset)
  sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=charset)
  sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=charset)


if __name__ == '__main__':
  # see here for more information.
  # https://docs.python.org/ja/3/library/re.html

  # Syntax
  """
  # an extension notation

  # flag
  (?:aiLmsux)
    a ascii
    i ignoreCase
    L locale
    m multiline
    s dot matches all
    u unicode matches
    x verbose

  # non-capturing
  (?:...)

  # flag
  (?aiLmsux-imsx:...)
  Zero or more letters from the set
  'a', 'i', 'L', 'm', 's', 'u', 'x',
  optionally followed by '-' followed by one or more letters from
  the 'i', 'm', 's', 'x'.

  # Accessible via the symbolic group name.
  (?P<name>...)

  # A backreference to a named group.
  (?P=name)

  # comment
  (?#...)

  # lookahead assertion
  # 例: abcd(?=Wxyz) は abcd に、その後に Wxyz が続く場合にのみマッチ。
  (?=...)

  # negative lookahead assertion
  # 例: abcd(?!Wxyz) は abcd に、その後に Wxyz が続かない場合にのみマッチ。
  (?!...)

  # positive lookbehind assertion
  (?<=...)

  # negative lookbehind assertion
  (?<!...)
  """

  # Flags
  # re.DEBUG
  # re.A | re.ASCII
  # re.I | re.IGNORECASE
  # re.L | re.LOCAL
  # re.M | re.MULTILINE
  # re.S | re.DORALL
  # re.X | re.VERBOSE

  # func
  # re.compile(pat, flags=0)
  # Compile a regular expression pattern into a regular expression object.

  # re.search(pat, str, flags=0)
  # Scan through string looking for the first matched pattern.
  # sreturn match object or None.

  # re.match(pat, str, flags=0)
  # Match a regexp pattern to the beginning of a string.
  # Return match object or None.

  # re.fullmatch(pat, str, flags=0)
  # Match a regexp pattern to all of a string.
  # Return match object or None.

  # re.split(pat, str, maxsplit=0, flags=0)
  # Split string by the occurrences of a pattern.
  # return a list.

  # re.findall(pat, str, flags=0)
  # Return a list of all non-overlapping matches in the string.

  # re.finditer(pat, str, flags=0)
  # Return an iterator over all non-overlapping matches in the string. the iterator returns a match object.

  # re.sub(pat, repl, str, count=0, flags=0)
  # Return a new string.

  # re.subn(pat, repl, str, count=0, flags=0)
  # Return tuple(new_string, num)

  # re.escape(pat)
  # Escape all chars except ASCII, number, _.

  # re.purge()
  # Clear the regexp cache.

  # exception re.error(msg, pattern=None, pos=None)
  # msg
  # pattern
  # pos
  # lineno
  # colno

  # Compile object
  # regexp.groups
  # regexp.groupindx
  # regexp.flags
  # regexp.pattern

  # Match object
  # match.expand(template)
  # match.group([g1, ...])
  # match.groups(default=None)
  # match.groupsict(default=None)
  # match.start([group])
  # match.end([group])
  # match.span([group])
  # match.pos
  # match.endpos
  # match.lastindex
  # match.lastgroup
  # match.re
  # match.string

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

  r = re.compile('<p>', re.S|re.M|re.I)
  print(r.search(html).span())
  print(r.match(html))

