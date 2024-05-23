import sys
args = sys.argv
#引数を変数に代入
input = int(args[1])

#素数かどうか判断する関数を設定
def prime(input):
    for i in range(2, input):
        #割り切れる数があるか
        if input % i == 0:
            return False

    return True

#1000以上の場合はエラー文の表示
if input >= 1000:
    print('1000以上は判定できません', end = '')
elif prime(input):
    print('Prime', end = '')
else:
    print('not', end = '')
