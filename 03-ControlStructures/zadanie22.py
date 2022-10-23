for i in range(1,31):
    if i%3==0 and i%5!=0:
        print("trzy",end=" ")
    elif i%5==0 and i%3!=0:
        print("piec",end=" ")
    elif i%3==0 and i%5==0:
        print("bingo",end=" ")
    else:
        print(i,end=" ")
        