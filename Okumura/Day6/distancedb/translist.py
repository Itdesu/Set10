from database import session
from create_transport import Transport
import sys

args = sys.argv

# 出力先パスを指定
path = r"output/output.txt"

# データベースからデータを取り出す
rows = session.query(Transport).all()

# Todo:SQL文は極力減らす(アクセスしすぎると不可かかる)

# 読み込んだデータを書き出す
with open(path, 'w', encoding="UTF-8") as f:
    for row in rows:
        list = f'"{row.date}", "{row.seq}", "{row.departure}", "{row.arrival}", "{row.via}", "{row.amount}" \n'
        f.write(list)