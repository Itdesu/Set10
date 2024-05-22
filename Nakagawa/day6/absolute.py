import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])

#絶対値への変換
absolute = abs(num)

#出力
print(f"{num} {absolute}", end = "")