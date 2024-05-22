from decimal import Decimal, ROUND_HALF_UP
from database import session
from tables import Stations


import sys
args = sys.argv

sta1=session.query(Stations).filter_by(name=args[1]).first()
sta2=session.query(Stations).filter_by(name=args[2]).first()

#距離の計算
if sta2.kilo>sta1.kilo:
    distance = sta2.kilo-sta1.kilo
else:
    distance = sta1.kilo-sta2.kilo

print(distance)