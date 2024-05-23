from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

# Create Table
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)

# CREATE TABLE transport (
#     date Date NOT NULL,
#     seq INT NOT NULL,
#     departure VARCHAR(20),
#     arrival VARCHAR(20),
#     via VARCHAR(40),
#     amount INT,
#     PRIMARY KEY (date, seq)
# );