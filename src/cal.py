# -*- coding: utf-8 -*-

import sys
import io
import traceback
import calendar

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
  
  y = 2018
  m = 12
  d = 1
  
  # firstweekday 0 is mon, 6 is sun.
  tc = calendar.TextCalendar(firstweekday=6)
  
  # 曜日の数字を1週間分を生成するイテレータを返す。
  for i in tc.iterweekdays():
    print(i)
  
  # 1ヶ月分を1週間単位でリストを返す。
  print(tc.monthdatescalendar(y, m))
  
  # fromatmonth(theyear, themonth, w=0, l=0)
  # w: 一日の間の文字間
  # l: 週と週の間の行間
  # 指定した一月分のカレンダーを返す。
  print(tc.formatmonth(y, m, w=3, l=2))
  
  # formatyear(theyear, themonth, w=2, l=1, c=6, m=3)
  # w: 一日の間の文字間
  # l: 週と週の間の行間
  # c: 月と月の間のスペース
  # m: 1行あたり出力する月の数
  print(tc.formatyear(y, c=1, m=2))
  
  # pmonth(theyear, themonth, w=0, l=0)
  # formatmonth で返した内容を出力する。
  tc.prmonth(y, m)
  
  # pyear(theyear, themonth, w=2, l=1, c=6, m=3)
  # formatyear で返した内容を出力する。
  tc.pryear(y, c=1, m=2)
  
  # 指定した年月の週を datetime.date 形式のリストで返す。
  # monthdatescalendar(year, month)
  print(tc.monthdatescalendar(y, m))
  
  # 指定した年月の週の日付と曜日番号を tuple 形式で返す。該当月にない日は、0 になる。
  # monthdays2calendar(year, month)
  print(tc.monthdays2calendar(y, m))
  
  # 指定した年月の週の日付を list 形式で返す。該当月にない日は、0 になる。
  # monthdayscalendar(year, month)
  print(tc.monthdayscalendar(y, m))
  
  # 指定した年のデータを datetime.date 形式のリストで返す。月の並べは最大 width ヶ月分の指定ができる。
  # yeardatescalendar(year, width=3)
  print(tc.yeardatescalendar(y))
  
  # 指定した年のデータの日付と曜日番号を tuple 形式で返す。該当ににない日は、0 になる。
  # yeardays2calendar(year, width=3)
  print(tc.yeardays2calendar(y))
  
  # 指定した年のデータの日付を list 形式で返す。該当月にない日は、0 になる。
  # yeardayscalendar(year, width=3)
  print(tc.yeardayscalendar(y))
  
  
  # Other calendar object
  hc = calendar.HTMLCalendar()
  print(hc.formatmonth(y, m))
  
  # LocaleTextCalendar(firstweekday=0, locale=None)
  # LocaleHTMLCalendar(firstweekday=0, locale=None)
  
  # 閏年の確認
  print(calendar.isleap(y))
  
  # 指定した範囲の中で何回閏年があるかを返す。
  # calendar.leapdays(y1, y2)
  print(calendar.leapdays(y, y +10))
  
  # 曜日を返す。
  # 0=mon, ..., 6=sun
  print(calendar.weekday(y, m, d))
  
  # 曜日のヘッダを返す。
  # n: ヘッダの文字数
  print(calendar.weekheader(3))
  
  # 指定した月の最初の日の曜日と日数を tuple 形式で返す。
  print(calendar.monthrange(y, m))
  
  # 指定した月の日をリスト形式で返す。
  print(calendar.monthcalendar(y, m))
  
  # TextCalendar の prmonth() と同じ。
  calendar.prmonth(y, m, w=0, l=0)
  
  # TextCalendar の formatmonth() と同じ。
  print(calendar.month(y, m, w=0, l=0))

  # TextCalendar の pryear()
  calendar.prcal(y, w=0, l=0, c=6, m=3)

  # TextCalendar の formatyear() と同じ。
  print(calendar.calendar(y, w=2, l=1, c=6, m=3))
  
  # Unix タイムスタンプの値を返します。
  # tuple(yyyy, mm, dd, h, m, s)
  # calendar.timegm(tuple)
  print(calendar.timegm((y, m, d, 0, 0, 0)))
  # 現在のロケールでの曜日を表す配列。
  print(calendar.day_name[0])

  # 現在のロケールでの短縮された曜日を表す配。
  print(calendar.day_abbr[0])

  # 現在のロケールでの月の名を表す配列。
  # 1-12
  print(calendar.month_name[1])
  
  # 現在のロケールでの短縮された月の名を表す配列。
  # 1-12
  print(calendar.month_abbr[1])
