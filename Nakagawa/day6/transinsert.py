import sys
from datetime import date
from database import session
from tables import Transport
args = sys.argv
#引数を変数に代入
input_date = args[1]
input_seq = int(args[2])
input_departure = args[3]
input_arrival = args[4]
input_via = args[5]
input_amount = args[6]

#日付の分解
#年
year = int(input_date[:4]) 
#月
if input_date[4] == '0':
    month = int(input_date[5])
else:
    month = int(input_date[4:5])
#日
day = int(input_date[-2:])

#日付型に変更したものを代入
dt = date(year, month, day) 
#重複しているもののレコードを取得
daylist = session.query(Transport).filter_by(data = dt).count()
seqlist = session.query(Transport).filter_by(seq = input_seq).count()

#重複がある場合、エラーの表示
if daylist > 0 or seqlist > 0:
        print("交通費精算テーブルにデータを登録できませんでした", end= '')
else:
    #登録するデータの編集
    transport = Transport(
        data = dt,
        seq = input_seq,
        departure = input_departure,
        arrival = input_arrival,
        via = input_via,
        amount = input_amount
    )

    #Insert処理
    session.add(transport)
    #登録内容のコミット
    session.commit()
    print('交通費精算テーブルにデータを登録しました', end = '')