import sys
from decimal import Decimal, ROUND_HALF_UP

def Calc_Sales_Profit(args):
    chicken = [760, 32.3]
    curry = [850, 28.4]
    # 唐揚げの数
    chicken_price = chicken[0] * int(args[1])
    curry_price = curry[0] * int(args[2])

    # カレーの数
    
    # 売り上げを計算
    sales = chicken_price + curry_price

    # 原価を計算
    chicken_cost = Decimal(chicken_price * chicken[1] / 100).quantize(Decimal('0'),ROUND_HALF_UP) 
    curry_cost = Decimal(curry_price * curry[1] / 100).quantize(Decimal('0'),ROUND_HALF_UP)

    cost = chicken_cost + curry_cost

    # 粗利を計算
    profit = sales - cost

    # Print
    print("売上高：" + str(sales) + "、原価：" + str(cost) + "、粗利：" + str(profit), end="") 

args = sys.argv

Calc_Sales_Profit(args)