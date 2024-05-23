import sys

# 初期値の設定
args = sys.argv
LUNCH = {"唐揚げ定食": 760, "カレーセット": 850}

# 売り上げを計算
sales = LUNCH["唐揚げ定食"] * int(args[1]) + LUNCH["カレーセット"] * int(args[2])

print(str(sales), end="")