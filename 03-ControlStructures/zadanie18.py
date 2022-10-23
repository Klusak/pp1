kwota=int(input("podaj kwote w pln: "))
piec=0
dwa=0
jeden=0
for i in range(kwota):
    if kwota>=5:
        piec+=1
        kwota-=5
    elif kwota>=2:
        dwa+=1
        kwota-=2
    elif kwota>=1:
        jeden+=1
        kwota-=1
print("kwota w monetach:")
print(f"5zl-{piec}")
print(f"2zl-{dwa}")
print(f"1zl-{jeden}")
