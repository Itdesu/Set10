from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv
#引数を変数に代入
chicken_num = int(args[1])   #唐揚げ定食の注文数
curry_num = int(args[2])     #カレーセットの注文数

#売上高
chicken_sales = 760 * chicken_num
curry_sales = 850 * curry_num
#一日の売上高
sales = chicken_sales + curry_sales
#原価
chicken_cost = chicken_sales * 0.323
chicken_cost = Decimal(str(chicken_cost)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
curry_cost = curry_sales * 0.284 
curry_cost = Decimal(str(curry_cost)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
#一日の原価
cost = chicken_cost + curry_cost
#粗利
profit = sales - cost

print(f'売上高：{sales}、原価：{cost}、粗利：{profit}', end = '')