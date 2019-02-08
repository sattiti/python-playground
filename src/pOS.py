# -*- coding: utf-8 -*-

import sys
import io
import traceback
import os

def std_encoding(charset):
    try:
        # sys.stdin  = codecs.getreader(sys.stdin.encoding)(sys.stdin)
        # sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
        sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding=charset)
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=charset)
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding=charset)
    except Exception as e:
        traceback.print_exc()
        pass

if __name__ == '__main__':
    std_encoding('utf-8')
    
    # os name
    print('os name: %s\n' % os.name)
    
    # environ
    print('environ:\n%s' % os.environ)
    
    # get env
    print("os.getenv('HOME'):  %s\n" % os.getenv('HOME'))
    print("os.environ['HOME']: %s\n" % os.environ['HOME'])
    
    # cwd
    print('cwd: %s\n' % os.getcwd())
    
    # uname
    print("uname: {}\n".format(os.uname()))
    
    # Return the name of the user logged in on the controlling terminal of the process.
    print('process name: %s\n' % os.getlogin())