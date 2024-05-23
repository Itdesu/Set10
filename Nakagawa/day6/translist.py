import sys
import os
from database import session
from tables import Transport
args = sys.argv
#引数を変数に代入
input = args[1]

#テーブルを全て取得
lists = session.query(Transport).all()
#レコードの数を取得
count = session.query(Transport).count()

#ファイルを開き、テキスト入力
with open(os.path.join('..', 'output', input), mode = 'w', encoding = 'utf-8') as f:
    #要素の数分繰り返し
    for list in lists:
        f.write(f'"{list.data}","{list.seq}","{list.departure}","{list.arrival}","{list.via}","{list.amount}"\n')