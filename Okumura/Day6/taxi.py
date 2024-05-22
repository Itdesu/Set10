import sys

args = sys.argv

distance = int(args[1])
fee = 630

# 630円分の距離を引く
distance -= 1500

while distance > 0:
    fee += 98
    distance -= 344

print(fee, end="")