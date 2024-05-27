import sys
from datetime import date
from database import session
from tables import Transport

args=sys.argv

transportlist = session.query(Transport).order_by(Transport.seq).all()
#ファイルを作成or開く
f = open(args[1], 'w')
#羊を数える
for transport in transportlist:
        # ファイルに書き込む
        line = f'"{transport.date.strftime("%Y-%m-%d")}", "{transport.seq}", "{transport.depature}", "{transport.arrival}", "{transport.via}", "{transport.amount}"\n'        
        f.write(line)
#ファイルを閉じる
f.close()