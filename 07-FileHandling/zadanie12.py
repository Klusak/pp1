produkt=input("dodaj nowy produkt: ")
file=open('shopping_list.txt','a',encoding='utf-8')
file.write(produkt)
file.write("\n")
file.close()