drinks = {"お茶":110,"コーヒー":100,"ソーダ":160,"コーンポタージュ":130}

#おつりを返す関数
def split_coins(amount):
    num_5000 = amount // 50000
    amount -= num_5000 * 5000

    num_1000 = amount // 1000
    amount -= num_1000 * 1000

    # 500円玉の枚数を計算
    num_500 = amount // 500
    amount -= num_500 * 500

    # 100円玉の枚数を計算
    num_100 = amount // 100
    amount -= num_100 * 100

    # 50円玉の枚数を計算
    num_50 = amount // 50
    amount -= num_50 * 50

    # 10円玉の枚数を計算
    num_10 = amount // 10

    # 0枚のコインは表示しない
    result = []
    if num_5000 > 0:
        result.append(f"5000円札: {num_5000}枚")
    if num_1000 > 0:
        result.append(f"1000円札: {num_1000}枚")
    if num_500 > 0:
        result.append(f"500円玉: {num_500}枚")
    if num_500 > 0:
        result.append(f"500円玉: {num_500}枚")
    if num_100 > 0:
        result.append(f"100円玉: {num_100}枚")
    if num_50 > 0:
        result.append(f"50円玉: {num_50}枚")
    if num_10 > 0:
        result.append(f"10円玉: {num_10}枚")

    return result

def Repeat(amount):
    for name,price in drinks.items():
        output = "{0}:{1}円".format(name,price)
        print(output)
    item=input("何を購入しますか（商品名/cancel）")
    if item=="cancel":
        print(amount)

    amount=amount-drinks[item]

    if amount>=100:
        print("残金:"+str(amount)+"円")
        judge=input("続けて表示しますか（Y/N）") 
    
        if judge=="Y":
            Repeat(amount)
    return 0

def otsuri(balance):
    print("おつり")
    coin_counts = split_coins(balance)
    print(coin_counts)        
    

#処理1(商品のを出力し、投入金額を入力させる)
for name,price in drinks.items():
    output = "{0}:{1}円".format(name,price)
    print(output)
x = input("投入金額を表示してください: ")
#処理5
x=int(x)
y=x%10
if y!=0:
    print("1円玉、5円玉は使用できません。再度投入金額を入力してください")

else:
    #処理2
    if x>=100:
        item=input("何を購入しますか（商品名/cancel）")
        if item=="cancel":
            print(x)
    #処理3
    elif x>10000:
        print("10000円を超える金額は購入できません。再度金額を入力してください")
    #処理4
    elif x<100:
        print(str(x)+"円は購入できる商品がありません。再度投入金額を入力してください")
#処理6-1
balance=x-drinks[item]
if balance>=100:
    print("残金:"+str(balance)+"円")
    judge=input("続けて表示しますか（Y/N）")
    if judge=="Y":
        Repeat(balance)
        otsuri(balance)
    else:
        otsuri(balance)


#処理6-3,処理6-4
else:
    otsuri(balance)

    




