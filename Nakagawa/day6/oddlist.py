#リストを生成
namelist = ["Kurita", 
            "Tanaka", 
            "Kaneda", 
            "Noda", 
            "Koyama", 
            "Adachi", 
            "Kuriyama", 
            "Ohyama", 
            "Kishida"]

#結果を入れる空のリストの生成
result = []

#奇数のものをリストに追加を要素の数だけ繰り返す
for i in range(1, len(namelist)):
    if i % 2 == 1:
       result.append(namelist[i])

print(result, end = '')