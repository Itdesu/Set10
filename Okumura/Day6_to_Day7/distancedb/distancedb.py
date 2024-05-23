import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import session
from create_distance import Stations

args = sys.argv

station_1 = session.query(Stations).filter_by(name=args[1]).first()
station_2 = session.query(Stations).filter_by(name=args[2]).first()

print(station_1.kilo)

distance = station_1.kilo - station_2.kilo
distance = abs(distance)
print(str(distance))