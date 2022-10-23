wiek_psa=int(input("podaj wiek psa: "))
if wiek_psa<=2:
    wiek_psa*=10.5
    print("wiek psa liczony w psich latach jest rowny 10,5 lat")
else:
    wiek_psa=(wiek_psa-2)*4+21
    print(f"wiek psa liczonych w psich latach jest rowny {wiek_psa}")