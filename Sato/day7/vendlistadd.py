from database import session
from tables import Mst_merchandise,Tbl_stock

import sys
args=sys.argv

# merchandise = Mst_merchandise(
#     id=args[1],
#     name=args[2],
#     price=int(args[3]),
# )

stock = Tbl_stock(
     id=args[1],
     stock=args[2],
)

session.add(stock)
session.commit()