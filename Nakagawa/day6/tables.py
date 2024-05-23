import sys
from sqlalchemy import Column, String, Numeric, Integer, Date
from database import Base
from database import ENGINE

#テーブル：stationsの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))

#テーブル：transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    data = Column('data', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(20))
    amount = Column('amount', Integer)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)