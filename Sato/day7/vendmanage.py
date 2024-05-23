import sys
from datetime import date
from database import session
from tables import Mst_merchandise

merchandiselist = session.query(Mst_merchandise).all()
#ファイルを作成or開く
#羊を数える
for merchandise in merchandiselist:
        # ファイルに書き込む
        print(f'{merchandise.name}:{merchandise.price}')   

x=input("投入金額を表示してください: ")

#処理1
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
