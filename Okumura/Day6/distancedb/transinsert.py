from database import session
from create_transport import Transport
import sys

args = sys.argv

date = session.query(Transport).filter_by(date = args[1])
seq = session.query(Transport).filter_by(date = args[2])

if date != None and seq != None:
    print("error:交通費精算テーブルにデータを登録できませんでした")

else:
    transport = Transport(
        date = args[1],
        seq = args[2],
        departure = args[3],
        arrival = args[4],
        via = args[5],
        amount = args[6],
    )
    session.add(transport)
    session.commit()