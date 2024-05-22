import sys
args = sys.argv
#引数を変数に代入
chicken_num = int(args[1])   #唐揚げ定食の注文数
curry_num = int(args[2])     #カレーセットの注文数

#唐揚げ定食の売上高
chicken_sales = 760 * chicken_num
#カレーセットの売上高
curry_sales = 850 * curry_num
#一日の売上高
sales = chicken_sales + curry_sales

print(sales, end = '')
