import sys
from database import session
from tables import Stations

args = sys.argv
#引数を変数に代入
st_start = args[1]
st_last = args[2]

# 引数と一致する駅名があるレコードを取得する
startlist = session.query(Stations).filter_by(name = st_start).first()
lastlist = session.query(Stations).filter_by(name = st_last).first()

#引数間の距離の計算
distance = abs(lastlist.kilo - startlist.kilo)
#小数点第二位で四捨五入
distance = round(distance, 2)

print(distance, end = '')