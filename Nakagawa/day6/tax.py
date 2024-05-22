import sys
args = sys.argv
#引数を変数に代入
dis = int(args[1])

#初乗り運賃
price = 630

#距離の差分の計算
price_up = dis - 1500

#追加料金
if dis >= 1500:
    #344m毎の計算
    price += 98 * ((price_up + 344 - 1) // 344)
    
#出力
print(price, end = "")