n=int(input("wprowadz n: "))
ilosc=0
test=1
while ilosc<n:
    test+=1
    czy_pierwsza="tak"
    for i in range(2,test-1):
        if test%i==0:
            czy_pierwsza="nie"
    if czy_pierwsza=="tak":
        ilosc+=1
        print(test,end=" ")
    