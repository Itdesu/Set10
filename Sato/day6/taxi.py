import sys
args=sys.argv
distance=args[1]

distance=int(distance)

#運賃の計算
fee=630
#距離を1500m引く
distance=distance-1500

#1500より大きければ98円足す

while 0<distance:
    distance=distance-344
    fee=fee+98

print(fee)
