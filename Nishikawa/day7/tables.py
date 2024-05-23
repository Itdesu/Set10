import sys
from sqlalchemy import Column, String, Integer,Numeric
from Nishikawa.day7.database import Base
from Nishikawa.day7.database import ENGINE

#テーブル：stationsの定義
class stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)