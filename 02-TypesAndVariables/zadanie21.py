def czy_rowne(a,b):
    if a!=b:
        return False
    return True

import random
a=random.randint(1,6)
b=int(input("wprowadz liczbe od 1 do 6: "))
if a==b:
    print(True)