import sys
args=sys.argv
num=args[1]
num=int(num)

if num<0:
    absolute=0-num
else:
    absolulte=num

print(num,absolute,end="")