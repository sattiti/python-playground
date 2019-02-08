# -*- coding: utf-8 -*-

import sys
import io
import traceback
from pathlib import Path

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
  
  html = Path('res/index.html')
  
  # py version
  crt_ver = float(('%d.%d' % (sys.version_info.major, sys.version_info.minor)))
  
  # user home
  home = Path.home()
  
  # absolute path
  script_file = Path(__file__).resolve()
  
  
  # file path
  print("script_file: %s\n" % script_file)
  
  # dirname
  print("dirname: %s\n" % script_file.parent)
  
  # basename
  print("basename: %s\n" % script_file.name)
  
  # ext
  print("ext: %s\n" % script_file.suffix)
  
  # ext list
  print('exts: {}\n'.format(script_file.suffixes))
  
  # filename
  print("stem: %s\n" % script_file.stem)
  
  # parts
  print('parts: {}\n'.format(script_file.parts))
  
  # parents
  print('parents: {}\n'.format(home.parents[0]))
  
  # root
  print('root: %s\n' % script_file.root)
  
  # absolute path
  print('absolute: %s\n' % home.absolute())
  
  # match
  print('match: {}\n'.format(home.match('*.py')))
  
  # relative_to
  print('relative: {}\n'.format(script_file.relative_to(__file__)))
  
  # drive
  print('drive: {}\n'.format(script_file.drive))
  
  # drive + root path
  print('anchor: %s\n' % home.anchor)
  
  # uri format
  print('uri: %s\n' % home.as_uri())
  
  # posix format
  print('posix: %s\n' % home.as_posix())
  

  # home directory
  print('home: %s\n' % home)
  
  # cwd
  print("cwd: %s\n" % Path.cwd())
  

  # stat
  print('stat: {}\n'.format(script_file.stat()))
  
  # lstat
  # stat() と同じだが、リンク先がシンボルリックリンクの場合、シンボルリックリンクの情報を返す。
  print('lstat: {}\n'.format(script_file.lstat()))
  
  # return the group name.
  print('belongs group: {}\n'.format(script_file.group()))
  
  # owner
  print('owner: {}\n'.format(script_file.owner()))
  

  # glob
  # Path.rglob(pattern) 再帰
  print('glob:')
  for f in script_file.parent.glob('**/*.xml'):
    print(f)
  print()
  
  # iterdir()
  # していしたディレクトリ内の内容を返す
  for f in home.iterdir():
    print(f)
  print()


  # joinpath
  print('joinpsth: %s\n' % script_file.parent.joinpath('aaa.html'))
  
  # with_name
  # 現在パスの name の部分を変換して返す。
  # 元のパスに name がない場合、ValueError を返す。
  print('with_name: %s\n' % script_file.with_name('script.py'))
  
  # with_suffix
  # ext 変更
  print('with_suffix: {}\n'.format(script_file.with_suffix('.txt')))


  # expanduser()
  # expand ~
  print('expanduser: {}\n'.format(Path('~').expanduser()))
  
  # exists
  print('exists: {}\n'.format(script_file.with_name('script').exists()))
  
  # samefile
  print('samefile: {}\n'.format(script_file.samefile(html)))


  # is_absolute()
  print('is_abs: {}\n'.format(script_file.is_absolute()))
  
  # is_reserved
  print('is_reserved: {}\n'.format(script_file.is_reserved()))
 
  # is_dir 
  print('{} is a dir: {}\n'.format(home.name, home.is_dir()))
  
  #is_file
  print('{} is a file: {}\n'.format(home.name, script_file.is_file()))
  
  # is_mount
  if crt_ver >= 3.7:
    print('{} is mount: {}\n'.format(home.name, script_file.is_mount()))
  
  # is_symlink
  print('symlink: {}\n'.format(script_file.is_symlink()))
  
  # fifo
  print('fifo: {}\n'.format(script_file.is_fifo()))
  
  # block_device
  print('block_device: {}\n'.format(script_file.is_block_device()))
  
  # char_device
  print('char_device: {}\n'.format(script_file.is_char_device()))

  
  # chmod
  # script_file.chmod(0o775)
  # print('mod: {}\n'.format(oct(script_file.stat().st_mode)))
  
  # lchmod(mode)
  # chmod() と同じ。しんぼリックリンクの場合、しんぼリックリンクに対して変更する。
  
  # mkdir
  # Path.mkdir(mode=0o777, parents=False, exist_ok=False)
  
  # rmdir
  # Path.rmdir()
  
  # rename
  # Path.rename(target)
  
  # replace
  # Path.replace(target)
  
  # create a symlink
  # Path.symlink_to(target, target_is_directory=False)
  
  # touch
  # Path.touch(mode=0o666, exist_ok=True)
  
  # rm
  # Path.unlink()
  
  # open
  # Path.open(mode='home', buffering=-1, encoding=None, errors=None, newline=None)
  
  
  # read_bytes()
  print('{}\n'.format(html.read_bytes()))
  
  # read_text(encoding=None, errors=None)
  print('{}\n'.format(html.read_text(encoding='utf-8')))
  
  # write_bytes()
  # Path.write_bytes(data)
  
  # write text
  # Path.write_text(data, encoding=None, errors=None)