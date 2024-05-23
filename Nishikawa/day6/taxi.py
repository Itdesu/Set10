import sys
args=sys.argv

kyori=int(args[1])

if kyori <= 1500:
    fare = 630
else:
    fare = (((kyori-1500)+344-1)//344)*98+630

print(fare,end="")