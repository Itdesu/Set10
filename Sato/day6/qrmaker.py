import qrcode
import sys
args = sys.argv

i=1
while i < len(args):
    url = args[i]
    img = qrcode.make(url)
    img.save(f"{i}.png")
    i += 1