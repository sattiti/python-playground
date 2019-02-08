# -*- coding: utf-8 -*-

import sys
import io
import traceback
import time
from datetime import  datetime

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
  
  # datetime.datetime.now()
  n = datetime.now()
  print(n)
  print(n.year)
  print(n.month)
  print(n.day)
  print(n.hour)
  print(n.minute)
  print(n.second)
  print(n.microsecond)
  print(n.ctime())
  print(n.date())
  print(n.dst())
  print(n.fold)
  print(n.time())
  print(n.timestamp())
  print(n.timetuple())
  print(n.timetz())
  print(n.today())
  print(n.toordinal())
  print(n.tzinfo)
  print(n.tzname())
  print(n.strftime('%Y-%m-%d %H:%M:%S'))
  print(n.strptime('2018/1/1 00:00:01', '%Y/%m/%d %H:%M:%S'))
  print(n.utcnow())
  print(n.utcoffset())
  print(n.utctimetuple())
  print(n.weekday())
  print(n.astimezone())
  print(n.isocalendar())
  print(n.isoweekday())
  
  # format codes
  # Weekday
  # %a Weekday as locale’s short name.
  # %A Weekday as locale’s full name.
  # %w Weekday as a decimal number, where 0 is Sun and 6 is Sat.
  
  # Day
  # %d Day of the month as a zero-padded decimal number. 01, 02, .., 31
  # %j Day of the year as a zero-padded decimal number. 001, 002, .., 366
  
  # Month
  # %b Month as locale’s short name.
  # %B Month as locale’s full name. 
  # %m Month as a zero-padded decimal number. 01, 02, .., 12
  # %U Week number of the year
  # %W Week number of the year
  
  # Year
  # %y Year without century as a zero-padded decimal number. 00, 01, .., 99
  # %Y Year with century as a decimal number. 0001, .., 2014, .., 9999
  
  # Hour
  # %H Hour (24-hour clock) as a zero-padded decimal number. 00, 01, .., 23 
  # %I Hour (12-hour clock) as a zero-padded decimal number. 01, 02, .., 12
  # %p Locale’s equivalent of either AM or PM.
  
  # Minute
  # %M Minute as a zero-padded decimal number. 00, 01, .., 59
  
  # Second
  # %S Second as a zero-padded decimal number. 00, 01, .., 59
  
  # Microsecond
  # %f Microsecond as a decimal number, zero-padded on the left. 000000, 000001, .., 999999
  
  # UTC
  # %z UTC offset in the form ±HHMM[SS[.ffffff]]
  
  # Timezone
  # %Z Time zone name
  
  # Other
  # %c Locale’s appropriate date and time representation.
  # %x Locale’s appropriate date representation.
  # %X Locale’s appropriate time representation.
  # %% A literal '%' character. %
