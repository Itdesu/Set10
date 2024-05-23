import sys
args=sys.argv

num=int(args[1])

if num >= 1000:
    print("1000以上は判定できません",end="")
    sys.exit()

check = 0  #0が立っていたらprime
for i in range(2,num):
    if num % i == 0:
        check = 1  #1が立っていたらnot
        break

if check == 1:
    print("not",end="")
else:
    print("Prime",end="")