# -*- coding: utf-8 -*-

from pathlib import Path
import io
import os
import sys
import shutil

sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

target = [
  "%s/.cache" % Path.home(),
  "%s/AppData/Local/ElevatedDiagnostics" % Path.home(),
  "%s/AppData/Local/Google/Chrome/User Data/Default/Cache" % Path.home(),
  "%s/AppData/Local/Microsoft/Windows/PowerShell/CommandAnalysis" % Path.home(),
  "%s/AppData/Local/Temp" % Path.home(),
  "%s/AppData/Local/pip/cache/http" % Path.home(),
  "%s/AppData/Roaming/Microsoft/Access/TemplateCacheFiles" % Path.home(),
  "%s/AppData/Roaming/Microsoft/Excel" % Path.home(),
  "%s/AppData/Roaming/Mozilla/Firefox/Crash Reports" % Path.home(),
  "%s/AppData/Roaming/npm-cache" % Path.home(),
  "/ProgramData/Microsoft/Windows/Caches"
  "/Windows/Temp",
]

for t in target:
    dist = t
    for f in list(Path(dist).glob('**/*')):
        if Path(f).is_file() and os.access(f, os.X_OK|os.R_OK|os.W_OK):
            try:
                Path(f).unlink()
            except Exception as e:
                pass
