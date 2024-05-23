import sys
args=sys.argv

karaage=int(args[1])
curry=int(args[2])

sales=760*karaage + 850*curry
print(sales,end="")