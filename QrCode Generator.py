import pyqrcode
import png
from pyqrcode import QRCode

a="https://github.com/likhithabasani/password-strength-checker/blob/main/passwordchecker.py"
url =pyqrcode.create(a)

 url.avg("nag.svg",scale=0)

 url.png('nag.png',scale=6)
