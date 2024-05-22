from datetime import date
from database import session
from tables import Transport

import sys
args=sys.argv

transport = Transport(
    date=args[1],
    seq=int(args[2]),
    depature=args[3],
    arrival=args[4],
    via=args[5],
    amount=args[6],
)

#同じ日付の検索
date_judge = session.query(Transport).filter_by(date = args[1]).first()



if date_judge.seq==int(args[2]):
    print("error:交通費精算テーブルにデータを登録できませんでした")
    
else:
    session.add(transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました")    

    
    