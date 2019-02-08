# -*- coding: utf-8 -*-

import sys
import io
import traceback
import qrcode

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

    msg = 'https://github.com/sattiti'
    img = qrcode.make(msg)
    print(img.size)

    img.save('./out/qr0.png')

    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=10
    )
    qr.add_data(msg)
    qr.make()
    img = qr.make_image(fill_color='blue', back_color='#ffff00')
    img.save('./out/qr1.png')
