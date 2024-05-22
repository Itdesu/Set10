from decimal import Decimal, ROUND_HALF_UP

import sys
args=sys.argv
num_ord=args[1]
num_ord2=args[2]

num_ord=int(num_ord)
num_ord2=int(num_ord2)

#売り上げ
proceeds=760*num_ord+850*num_ord2
#原価
cost=760*0.323*num_ord + 850*0.284*num_ord2
#四捨五入
cost=Decimal(cost).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
#粗利
gross=proceeds-cost

output="売上高："+str(proceeds)+"、原価："+str(cost)+"、粗利："+str(gross)
print(output)


