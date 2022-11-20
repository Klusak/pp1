def sumacyfr(x):
    suma=0
    while x>0:
        suma+=x%10
        x//=10
    return suma
print(sumacyfr(7182))