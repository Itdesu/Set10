import sys
args=sys.argv
num=args[1]
num=int(num)

# 素数判定
def prime_judge(n):
    # 1 未満の数は素数ではない
    if n < 2:
        return 0
    
    # n までの数について割り切れる数があるか判定
    for i in range(2, n):
        # 割り切れる数がある場合、素数ではない
        if n % i == 0:
            return 0

    # 割り切れる数がない場合、素数である
    return 1

if num<1000:
    #関数に渡して素数判定
    judge=prime_judge(num)
    if judge==1:
        print("Prime",end="")
    else:
        print("not",end="")
else:
    print("1000以上は判定できません",end="")