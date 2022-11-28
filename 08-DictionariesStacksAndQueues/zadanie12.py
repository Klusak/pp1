import json
fav_book={
    'tytul':'Trylogia Hell',
    'autor':'P.S.Herytiera',
    'ilosc_czesci': 3,
    'glowni_bohaterowie':['Victoria Clark','Nathaniel Shey'],
    'czy_polecam':True
}
file=open("favourite.json",'w')
json.dump(fav_book,file,indent=4)
file.close()
