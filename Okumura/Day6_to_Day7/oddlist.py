list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

i = 0
print("[",end="")

while i < len(list) - 2:
    if i % 2 != 0:
        print("'" + str(list[i]) + "', ",end="")
    i += 1
print("'" + str(list[i]) + "']",end="")