suma=0
ilosc=0
while True:
    liczba=int(input("wprowadz liczbe: "))
    suma+=liczba
    ilosc+=1
    if liczba==0:
        ilosc-=1
        break
srednia=suma/ilosc
print(f"ilosc={ilosc} suma={suma} srednia={srednia}") 