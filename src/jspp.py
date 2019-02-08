# -*- coding: utf-8 -*-
import jsbeautifier
import io
import sys
from pathlib import Path

sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

jsFiles = ('top', 'app')

for f in jsFiles:
    js  = Path("./%s.js" % f).open("r", encoding="utf-8")
    res = jsbeautifier.beautify(str(js.read()))
    Path("./%s-src.js" % f).open('w', encoding="utf-8").write(res)
