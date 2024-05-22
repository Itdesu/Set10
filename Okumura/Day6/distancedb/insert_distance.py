from database import session
from create_distance import Stations

stations = Stations(
    # seq = 1, name = "東京", kilo = 0.00,
    # seq = 2, name = "品川", kilo = 6.78,
    # seq = 3, name = "新横浜", kilo = 342.02,
    # seq = 4, name = "名古屋", kilo = 476.31,
    # seq = 5, name = "新大阪", kilo = 515.35,
)

session.add(stations)
session.commit()