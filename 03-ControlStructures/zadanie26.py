pin="0805"
for i in range(3):
    pin_uzyt=str(input("podaj pin: "))
    if pin!=pin_uzyt:
        print("zly pin")
        if i==2:
            print("karta zablokowana")
    else:
        print("pin poprawny")