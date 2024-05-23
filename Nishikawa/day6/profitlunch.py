import sys
args=sys.argv

from decimal import Decimal,ROUND_HALF_UP
karaage=int(args[1])
curry=int(args[2])

sales_karaage=(760*karaage)  #からあげ売上高
sales_curry=(850*curry)  #カレー売上高

sales=sales_karaage+sales_curry  #売上高合計

cost=Decimal(str(sales_karaage*0.323)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)+Decimal(str(sales_curry*0.284)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)  #原価

profit=sales-cost #粗利

print("売上高："+str(sales),"、原価："+str(cost),"、粗利："+str(profit),end="")
